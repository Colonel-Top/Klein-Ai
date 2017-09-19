import tensorflow as tf
import data_utils
import seq2seq_model

def train():
    #prepare dataset
    enc_train, dec_train = data_utils.prepare_custom (gConfig['working_directory'])
    train_set = read_data(enc_train,dec_train)

def seq2seq_f (encoder_inputs,decoder_inputs,do_decode):
    return tf.nn.seq2sea.embedding_attention_seq2seq(
        encoder_inputs, decoder_inputs, cell,
        num_encoder_symbols = source_vocabs_size,
        num_decoder_symbols = target_vocabs_size,
        embedding_size = size,
        output_projection = output_projection,
        feed_previous=do_decode)
with tf.Session(config=config) as sees:
    #create model
    model = create_model(sess,False)
    while True:
        sess.run(model)

        #save Checkpoint and zero timer and loss
        checkpoint_path = os.path.join(gConfig['working_directory'],"seq2seq.ckpt")
        model.saver.save(sess,checkpoint_path,global_step = model.global_step)
