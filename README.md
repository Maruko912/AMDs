# A-Comprehensive-Study-of-Learning-based-Android-Malware-Detectors-under-Challenging-Environments
## Abstarct

Recent years have witnessed the proliferation of learning-based Android malware detectors. These detectors can be categorized into three types, String-based, Image-based and Graph-based. Most of them have achieved good detection performance under the ideal setting. In reality, however, detectors often face out-of-distribution samples due to the factors such as code obfuscation, concept drift (e.g., software development technique evolution and new malware families emergence), and adversarial examples (AEs). This problem has attracted increasing attention, but there is a lack of comparative studies that evaluate the existing various types of detectors under these challenging environments. In order to fill this gap, we select 12 representative detectors from three types of detectors, and evaluate them in the challenging scenarios involving code obfuscation, concept drift and AEs, respectively. Experimental results reveal that none of the evaluated detectors can maintain their ideal-setting detection performance, and the performance of different types of detectors varies significantly under various challenging environments. We identify several factors contributing to the performance deterioration of detectors, including the limitations of feature extraction methods and learning models. We also analyze the reasons why the detectors of different types show significant performance differences when facing code obfuscation, concept drift and AEs. Finally, we provide practical suggestions from the perspectives of users and researchers, respectively. We hope our work can help understand the detectors of different types, and provide guidance for enhancing their performance and robustness.

## Flies

The paper: `A Comprehensive Study of Learning-based Android Malware Detectors under Challenging Environments.pdf`

The supplementary material of paper: `Supplementary_Material.pdf`

## DataSet

#### Data-MD

Data-MD can be downloaded from [Androzoo home (uni.lu)](https://androzoo.uni.lu/) by providing the apk's *sha256* and *apikey*. The `Data-MD` provides the sha256 list of our Data-MD dataset . The API needs to be requested from Androzoo. 

```
url_apk="https://androzoo.uni.lu/api/download?apikey=${APIKEY}&sha256=${SHA256}"
```

* Data-MD/train.txt: the *year*, *SHA256*, and *label* of the training samples.

* Data-MD/test.txt:  the *year*, *SHA256*, and *label* of the test samples.

```
 Example data:
   ['Years\\2020\\72334F6214BA86964437EA7D6259F6ADA8C4F6CE4BED1273427E1C9B396CC074', 1]
```

* `get_sha256_list.py`:  the script that can extract the list of *SHA256* from the *.txt* file

* Data-MD/test_ob.txt: the *year*, *SHA256*, and *label* of the obfuscated test samples.

#### Data-MC

Data-MC is downloaded from *CICDroid2020* and can be downloaded from this link https://www.unb.ca/cic/datasets/maldroid-2020.html. 

## Reference

```
@INPROCEEDINGS {gao2024AMDs,
author = {C. Gao and G. Huang and H. Li and B. Wu and Y. Wu and W. Yuan},
booktitle = {2024 IEEE/ACM 46th International Conference on Software Engineering (ICSE)},
title = {A Comprehensive Study of Learning-based Android Malware Detectors under Challenging Environments},
year = {2024},
volume = {},
issn = {1558-1225},
pages = {104-116},
publisher = {IEEE Computer Society},
address = {Los Alamitos, CA, USA},
month = {apr}
}
```

