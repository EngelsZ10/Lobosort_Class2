import tensorflow as tf
from tensorflow.keras.layers import GRU, Dense, Input, GlobalAveragePooling1D, LayerNormalization, MultiHeadAttention, Dropout
from tensorflow.keras.models import Model

class AttentionBlock(tf.keras.layers.Layer):
    def __init__(self, num_heads, key_dim, rate=0.1, **kwargs):
        super().__init__(**kwargs)
        self.attention = MultiHeadAttention(num_heads=num_heads, key_dim=key_dim)
        self.norm = LayerNormalization(epsilon=1e-6)
        self.dropout = Dropout(rate)

    def call(self, inputs, training=None):
        attn_output = self.attention(inputs, inputs)
        attn_output = self.dropout(attn_output, training=training)
        return self.norm(inputs + attn_output)
    
    def get_config(self):
        config = super().get_config()
        config.update({
            "num_heads": self.attention.num_heads,
            "key_dim": self.attention.key_dim,
            "rate": self.dropout.rate,
        })
        return config

class build:
    @staticmethod
    def build_it(input_shape=(28, 28), gru_units=32, num_heads=2, key_dim=4, ff_dim=16, num_classes=10):
        inputs = Input(shape=input_shape)
        x = GRU(gru_units, return_sequences=True)(inputs)
        x = AttentionBlock(num_heads=num_heads, key_dim=key_dim)(x)
        x = GlobalAveragePooling1D()(x)
        x = Dense(ff_dim, activation="relu")(x)
        outputs = Dense(num_classes, activation="softmax")(x)

        model = Model(inputs=inputs, outputs=outputs)

        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        return model
