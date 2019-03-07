gcloud compute scp jupyter@my-gpu-instance:~/xray_full/data/kaggle/sample/images/models ~/projects/xray_full/data/kaggle/sample/images/ --zone=us-central1-c --recurse 
gcloud compute scp jupyter@my-gpu-instance:~/xray_full/data/kaggle/sample/images/export.pkl ~/projects/xray_full/data/kaggle/sample/images/ --zone=us-central1-c 
cp ~/projects/xray_full/data/kaggle/sample/images/models/* ~/projects/xray_full/dl_chestxray14/model_data/models/
cp ~/projects/xray_full/data/kaggle/sample/images/export.pkl ~/projects/xray_full/dl_chestxray14/model_data/