import hadoopy
import cluster
import time

# HDFS Paths with data of the form (unique_string, binary_image_data
data_root = '/user/brandyn/classifier_data/'

train_photos_path = data_root + 'train_photos'
train_nonphotos_path = data_root + 'train_nonphotos'
train_indoors_path = data_root + 'train_indoors'
train_outdoors_path = data_root + 'train_outdoors'
train_objects_path = data_root + 'train_objects'
train_nonobjects_path = data_root + 'train_nonobjects'
train_pr0n_path = data_root + 'train_pr0n'
train_nonpr0n_path = data_root + 'train_nonpr0n'
train_faces_path = data_root + 'train_faces'
train_nonfaces_path = data_root + 'train_nonfaces'

test_photos_path = data_root + 'test_photos'
test_nonphotos_path = data_root + 'test_nonphotos'
test_indoors_path = data_root + 'test_indoors'
test_outdoors_path = data_root + 'test_outdoors'
test_objects_path = data_root + 'test_objects'
test_nonobjects_path = data_root + 'test_nonobjects'
test_pr0n_path = data_root + 'test_pr0n'
test_nonpr0n_path = data_root + 'test_nonpr0n'
test_faces_path = data_root + 'test_faces'
test_nonfaces_path = data_root + 'test_nonfaces'


def train():
    # HDFS Paths for Output
    start_time = time.time()
    root = '/user/brandyn/tp/image_cluster/run-%f/' % start_time
    
    # Compute features for classifier train
    cluster.run_image_feature(train_photos_path, root + 'train_feat/photos', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_nonphotos_path, root + 'train_feat/nonphotos', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_indoors_path, root + 'train_feat/indoors', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_outdoors_path, root + 'train_feat/outdoors', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_objects_path, root + 'train_feat/objects', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_nonobjects_path, root + 'train_feat/nonobjects', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_pr0n_path, root + 'train_feat/pr0n', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_nonpr0n_path, root + 'train_feat/nonpr0n', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_faces_path, root + 'train_feat/faces', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(train_nonfaces_path, root + 'train_feat/nonfaces', 'meta_gist_spatial_hist', 256)

    # Label images # TODO make one run of this per feature type as the training assumes the features are homogeneous
    cluster.run_classifier_labels(root + 'train_feat/photos', root + 'train_feat/nonphotos', root + 'labels/photos',
                                  'photo', '', 'tp_photos_labels.js', 'svmlinear')
    cluster.run_classifier_labels(root + 'train_feat/indoors', root + 'train_feat/outdoors', root + 'labels/indoors',
                                  'indoor', '', 'tp_indoors_labels.js', 'svmlinear')
    cluster.run_classifier_labels(root + 'train_feat/objects', root + 'train_feat/nonobjects', root + 'labels/objects',
                                  'object', '', 'tp_objects_labels.js', 'svmlinear')
    cluster.run_classifier_labels(root + 'train_feat/pr0n', root + 'train_feat/nonpr0n', root + 'labels/pr0n',
                                  'pr0n', '', 'tp_pr0n_labels.js', 'svmlinear')
    cluster.run_classifier_labels(root + 'train_feat/faces', root + 'train_feat/nonfaces', root + 'labels/faces',
                                  'face', '', 'tp_faces_labels.js', 'svmlinear')

    # Train classifiers
    cluster.run_train_classifier([root + 'train_feat/photos', root + 'train_feat/nonphotos'], root + 'classifiers/photos', 'tp_photos_labels.js')
    cluster.run_train_classifier([root + 'train_feat/indoors', root + 'train_feat/outdoors'], root + 'classifiers/indoors', 'tp_indoors_labels.js')
    cluster.run_train_classifier([root + 'train_feat/objects', root + 'train_feat/nonobjects'], root + 'classifiers/objects', 'tp_objects_labels.js')
    cluster.run_train_classifier([root + 'train_feat/pr0n', root + 'train_feat/nonpr0n'], root + 'classifiers/pr0n', 'tp_pr0n_labels.js')
    cluster.run_train_classifier([root + 'train_feat/faces', root + 'train_feat/nonfaces'], root + 'classifiers/faces', 'tp_faces_labels.js')
    return '%f' % start_time


def predict(train_start_time='1308626598.185418'):
    start_time = time.time()
    train_root = '/user/brandyn/tp/image_cluster/run-%s/' % train_start_time
    root = '/user/brandyn/tp/image_cluster/run-%f/' % start_time

    cluster.run_image_feature(test_photos_path, root + 'test_feat/photos', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_nonphotos_path, root + 'test_feat/nonphotos', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_indoors_path, root + 'test_feat/indoors', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_outdoors_path, root + 'test_feat/outdoors', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_objects_path, root + 'test_feat/objects', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_nonobjects_path, root + 'test_feat/nonobjects', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_pr0n_path, root + 'test_feat/pr0n', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_nonpr0n_path, root + 'test_feat/nonpr0n', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_faces_path, root + 'test_feat/faces', 'meta_gist_spatial_hist', 256)
    cluster.run_image_feature(test_nonfaces_path, root + 'test_feat/nonfaces', 'meta_gist_spatial_hist', 256)

    cluster.run_predict_classifier([root + 'test_feat/photos'], train_root + 'classifiers/photos', root + 'test_predict/photos')
    cluster.run_predict_classifier([root + 'test_feat/nonphotos'], train_root + 'classifiers/photos', root + 'test_predict/nonphotos')
    cluster.run_predict_classifier([root + 'test_feat/indoors'], train_root + 'classifiers/indoors', root + 'test_predict/indoors')
    cluster.run_predict_classifier([root + 'test_feat/outdoors'], train_root + 'classifiers/indoors', root + 'test_predict/outdoors')
    cluster.run_predict_classifier([root + 'test_feat/objects'], train_root + 'classifiers/objects', root + 'test_predict/objects')
    cluster.run_predict_classifier([root + 'test_feat/nonobjects'], train_root + 'classifiers/objects', root + 'test_predict/nonobjects')
    cluster.run_predict_classifier([root + 'test_feat/pr0n'], train_root + 'classifiers/pr0n', root + 'test_predict/pr0n')
    cluster.run_predict_classifier([root + 'test_feat/nonpr0n'], train_root + 'classifiers/pr0n', root + 'test_predict/nonpr0n')
    cluster.run_predict_classifier([root + 'test_feat/faces'], train_root + 'classifiers/faces', root + 'test_predict/faces')
    cluster.run_predict_classifier([root + 'test_feat/nonfaces'], train_root + 'classifiers/faces', root + 'test_predict/nonfaces')
    return '%f' % start_time


def _score_prediction(pos_pred_path, neg_pred_path, classifier_name):
    tp, fp, tn, fn = 0, 0, 0, 0
    # Pos
    for image_hash, preds in hadoopy.readtb(pos_pred_path):
        for cur_classifier_name, ((cur_conf, cur_pol),) in preds.items():
            if classifier_name == cur_classifier_name:
                conf = cur_conf * cur_pol
                if conf >= 0:
                    tp += 1
                else:
                    fn += 1
    # Neg
    for image_hash, preds in hadoopy.readtb(neg_pred_path):
        for cur_classifier_name, ((cur_conf, cur_pol),) in preds.items():
            if classifier_name == cur_classifier_name:
                conf = cur_conf * cur_pol
                if conf >= 0:
                    fp += 1
                else:
                    tn += 1
    print('%s: [%d, %d, %d, %d]' % (classifier_name, tp, fp, tn, fn))
    print('%.3f %.3f' % (tp / float(tp + fn), tp / float(tp + fp)))
    return tp, fp, tn, fn


def score_predictions(test_start_time='1308630752.962982'):
    root = '/user/brandyn/tp/image_cluster/run-%s/' % test_start_time
    _score_prediction(root + '/test_predict/photos', root + '/test_predict/nonphotos', 'photo')
    _score_prediction(root + '/test_predict/indoors', root + '/test_predict/outdoors', 'indoor')
    _score_prediction(root + '/test_predict/objects', root + '/test_predict/nonobjects', 'object')
    _score_prediction(root + '/test_predict/pr0n', root + '/test_predict/nonpr0n', 'pr0n')
    _score_prediction(root + '/test_predict/faces', root + '/test_predict/nonfaces', 'face')
     

if __name__ == '__main__':
    train_start_time = train()
    test_start_time = predict(train_start_time)
    score_predictions(test_start_time)


