# tf_compat.py ---------------------------------------------------------------
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()                   #  ← enables 1.x graph mode, adds v1 symbols

# optional safety aliases (so old code still finds them)
tf.variable_scope   = tf.compat.v1.variable_scope
tf.get_variable     = tf.compat.v1.get_variable
tf.layers           = tf.compat.v1.layers
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Re-create just the bit of tf.contrib the old code expects
import types
tf.contrib = types.SimpleNamespace()                # fake top-level contrib
tf.contrib.layers = types.SimpleNamespace(
        variance_scaling_initializer=tf.keras.initializers.VarianceScaling)
# ------------------------------------------------------------