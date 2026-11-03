# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitFaceVerifyRequest(DaraModel):
    def __init__(
        self,
        app_quality_check: str = None,
        auth_id: str = None,
        birthday: str = None,
        callback_token: str = None,
        callback_url: str = None,
        camera_selection: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        certify_id: str = None,
        certify_url_style: str = None,
        certify_url_type: str = None,
        crop: str = None,
        enable_album_upload: str = None,
        enable_beauty: str = None,
        enable_tts: str = None,
        encrypt_type: str = None,
        face_contrast_picture: str = None,
        face_contrast_picture_url: str = None,
        face_guard_output: str = None,
        h_5degrade_confirm_btn: str = None,
        ip: str = None,
        meta_info: str = None,
        mobile: str = None,
        mode: str = None,
        model: str = None,
        need_multi_face_check: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        procedure_priority: str = None,
        product_code: str = None,
        rarely_characters: str = None,
        read_img: str = None,
        return_url: str = None,
        scene_id: int = None,
        suitable_type: str = None,
        ui_custom_url: str = None,
        user_id: str = None,
        validity_date: str = None,
        video_evidence: str = None,
        voluntary_customized_content: str = None,
    ):
        # Specifies whether to enable strict face quality detection in the SDK. Valid values:
        # 
        # - **Y**: Enables strict face quality detection.
        # 
        # - **N**: Does not enable strict face quality detection. This is the default value.
        # 
        # 
        # > 
        # > - If you enable this parameter, the SDK must integrate the [strict face quality detection module](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/description-of-sdk-package-clipping). Affected by strict quality detection, the success rate of face scanning may decrease.
        # > - Only Android SDK 2.3.24 and later are supported.
        self.app_quality_check = app_quality_check
        # The user authorization ID. The maximum length is 64 characters.
        self.auth_id = auth_id
        # The date of birth on the ID document.
        # 
        # This parameter is required when the **CertType** parameter is set to **PASSPORT** and the **Mode** parameter is set to **3**.
        self.birthday = birthday
        # The security token that you generate to prevent duplicate and tampered requests.
        # 
        # If you specify this parameter, the **CallbackToken** field is displayed in the callback URL.
        self.callback_token = callback_token
        # The callback URL for authentication result notifications. The default callback request method is GET. The callback URL must start with `https`. After the authentication is completed, the platform invokes this URL and automatically appends the `certifyId` and `passed` fields. The value of the `passed` field is the subcode. Example: `https://www.aliyun.com?callbackToken=1000004826&certifyId=shaxxxx&passed=200`.
        # 
        # <notice>
        # 
        # - The callback is triggered only when the authentication is completed, including both successful and failed authentications. If the authentication is abandoned, an abnormal break occurs, or the authentication is not performed, no notification is sent. We recommend that you invoke the query API operation to obtain the authentication details after you receive the callback notification if needed.
        # - The accessibility of the URL is verified before the API operation is invoked. If the URL does not support public network access, a 401 error is returned.
        # - The API operation must return HTTP status code 200 after the callback. Otherwise, a retry is triggered, and two callbacks are sent within 3 seconds.
        # 
        # </notice>
        self.callback_url = callback_url
        # Specifies whether to enable the camera selection feature. Valid values:
        # 
        # - **Y**: Enables the feature.
        # 
        # - **N**: Does not enable the feature. This is the default value.
        # 
        # > This feature takes effect only in the PC integration mode. After this feature is enabled, users can select a camera for authentication.
        self.camera_selection = camera_selection
        # The real name.
        self.cert_name = cert_name
        # The ID document number.
        self.cert_no = cert_no
        # The type of the ID document.
        # 
        # Only ID cards are supported. Set the value to IDENTITY_CARD.
        self.cert_type = cert_type
        # **[Deprecated]**
        # 
        # The CertifyId of a previous successful ID Verification. The photo used in the previous authentication is used as the comparison photo.
        # 
        # > You can specify only one of the following parameters to pass the image: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS.
        self.certify_id = certify_id
        # The type of the returned **CertifyUrl**. Valid values:
        # 
        # - **L**: Original long URL.
        # 
        # - **S** (default): Short URL.
        self.certify_url_style = certify_url_style
        # The device type of the Web SDK. Valid values: **WEB** and **H5**.
        # 
        # > Only Web SDK device types are supported.
        self.certify_url_type = certify_url_type
        # Specifies whether to allow face image cropping. By default, cropping is not allowed. Valid values:
        # 
        # - T: Cropping is allowed.
        # 
        # - F: Cropping is not allowed.
        # 
        # > If the requested image is not collected by the standard liveness detection SDK, we recommend that you allow face image cropping. After this feature is enabled, the requested image is cropped and corrected before the request is sent to the service.
        self.crop = crop
        # Specifies whether to allow album upload. Valid values: Y and N. Default value: N.
        self.enable_album_upload = enable_album_upload
        # Specifies whether to enable the beauty filter. Valid values: Y and N.
        self.enable_beauty = enable_beauty
        # Specifies whether to enable speech synthesis for H5 willingness authentication. Valid values: Y and N. Default value: Y.
        self.enable_tts = enable_tts
        # The encryption algorithm. Only the SM2 algorithm is supported.
        # 
        # After encrypted transmission is enabled, you must pass the encrypted CertName and CertNo. For more information about encryption, see [Parameter encryption](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/description-of-parameter-encryption#task-2229332).
        self.encrypt_type = encrypt_type
        # The Base64-encoded image.
        # 
        # > You can specify only one of the following parameters to pass the image: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS.
        self.face_contrast_picture = face_contrast_picture
        # The URL of the image in OSS. Only authorized OSS image URLs are supported.
        # 
        # > You can specify only one of the following parameters to pass the image: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS.
        self.face_contrast_picture_url = face_contrast_picture_url
        # The type of the Device Assistant tag. Set the value to **DeviceRisk**.
        # 
        # >
        # > - Outputting Device Assistant tags incurs additional fees. For more information, see [Value-added services](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/face-guard).
        # > - If you do not need to output Device Assistant tags, you can leave this parameter empty or do not pass it.
        self.face_guard_output = face_guard_output
        # Specifies whether to display the I Have Completed Authentication button on the H5 downgrade page after authentication is completed. Valid values:
        # - **Y**: Displays the button.
        # - **N** (default): Hides the button.
        self.h_5degrade_confirm_btn = h_5degrade_confirm_btn
        # The IP address of the user.
        self.ip = ip
        # The Metainfo environment parameter. You must obtain this parameter by using the client SDK.
        self.meta_info = meta_info
        # The mobile phone number of the user.
        self.mobile = mobile
        # The method to obtain the passport NFC verification elements. Valid values:
        # 
        # - **1**: User input. The end user manually enters the ID document element information by using the UI provided by the Alibaba Cloud SDK.
        # 
        # - **3**: External parameter input. The ID document element information is passed from external sources.
        # 
        # > When the NFC decoder decrypts the encrypted information of the passport chip, it needs to obtain three passport elements: name, date of birth, and expiration date.
        self.mode = mode
        # The liveness detection type. Valid values:
        # > Only the following liveness detection types are supported. Custom actions or combinations are not supported.
        # 
        # Description
        # Only the following liveness detection types are supported. Custom actions or combinations are not supported.
        # 
        # - **LIVENESS** (default): Blinking.
        # 
        # - **PHOTINUS_LIVENESS**: Blinking and colorful light reflection.
        # 
        # - **MULTI_ACTION**: Blinking and head turning (the order is random).
        # 
        # - **MOVE_ACTION** (recommended): Moving closer or farther and blinking.
        # 
        # - **MOVE_PHOTINUS**: Moving closer or farther and colorful light reflection.
        # 
        # > 
        # >- **The default liveness detection type** is supported in the following SDK versions:
        # >   - Android SDK 1.2.6 and later
        # >   - iOS SDK 1.2.4 and later
        # >   - Harmony SDK 1.0.0 and later
        # >- Other types are supported in the latest SDK versions for Android, iOS, and Harmony. We recommend that you integrate the latest SDK version.
        self.model = model
        # Specifies whether to intercept the request when multiple faces are detected on the terminal. Valid values:
        # 
        # - **Y**: Intercepts the request. The client prompts the user to scan the face again.
        # 
        # - **N** (default): Does not intercept the request. The largest face in the face scanning screen is sent to the server for security detection.
        self.need_multi_face_check = need_multi_face_check
        # The name of the authorized OSS bucket.
        # 
        # > You can specify only one of the following parameters to pass the image: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS.
        self.oss_bucket_name = oss_bucket_name
        # The name of the object in the authorized OSS bucket.
        # 
        # > You can specify only one of the following parameters to pass the image: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, and OSS.
        self.oss_object_name = oss_object_name
        # The unique identifier of the merchant request.
        # 
        # The value is a 32-character alphanumeric string. The first few characters are a custom abbreviation of the merchant, the middle part can be a period of time, and the last part can be a random or incremental sequence.
        self.outer_order_no = outer_order_no
        # The downgrade configuration when WebRTC or WebAssembly is incompatible during mobile H5 authentication. Valid values:
        # 
        # - **keep**: Downgrade is not supported. The result is directly returned.
        # 
        # - **url** (default): Downgrade is supported. The authentication URL is returned. The user opens or switches to a browser by using this URL for authentication.
        # 
        # - **video**: Downgrade is supported. The system camera is used to record a 3- to 5-second blinking video for authentication.
        # 
        # 
        # > 
        # > When the downgrade mode is set to video, the following features become invalid and product security is reduced. We recommend that you configure this mode only for security scenarios.
        # > - The liveness detection type setting does not take effect.
        # > - The VideoEvidence feature is not supported.
        self.procedure_priority = procedure_priority
        # The fixed value. The value of this parameter varies based on the product solution:
        # - APP authentication solution: Set the value to ID_PRO.
        # - Face liveness verification solution: Set the value to PV_FV.
        # - Liveness detection solution: Set the value to LR_FR.
        self.product_code = product_code
        # Specifies whether to enable the rare character mode. Valid values:
        # 
        # - **Y**: Enables the mode. Before authentication, an information input box appears. The user must enter the name with rare characters and the ID card number, and agree to the agreement before the authentication process starts.
        # 
        # - **N**: Does not enable the mode. This is the default value.
        self.rarely_characters = rarely_characters
        # Specifies whether to read the ID document photo. Valid values:
        # 
        # - **Y**: Reads the photo.
        # 
        # - **N**: Does not read the photo.
        # 
        # > If you need to use the face photo from the ID document in subsequent authentication steps, we recommend that you set this parameter to Y.
        self.read_img = read_img
        # The redirect URL for the merchant business page.
        self.return_url = return_url
        # The ID of the authentication scenario.
        self.scene_id = scene_id
        # The age-friendly configuration parameter. This parameter takes effect for each authentication request. You can select different parameters for each authentication request based on the business property, customer distribution, and operation attribute of your app. The following options are available. Default value: 0.
        # 
        # - **0**: Disables the age-friendly pattern for the current authentication request.
        # 
        # - **1**: Enables the age-friendly pattern for the current authentication request.
        # 
        # - **2**: Allows the user to select the pattern.
        # 
        # 
        # The end user can select the authentication pattern. The product guide page provides two authentication entries: Start Authentication and Senior Authentication Pattern. When the user selects Senior Authentication Pattern, the system enters the age-friendly pattern.
        # > 
        # > - The age-friendly parameter takes effect only when the liveness detection type **Model** is set to **LIVENESS** or **MULTI_ACTION**.
        self.suitable_type = suitable_type
        # The URL of the UI configuration file.
        # 
        # For the complete configuration, see [Web SDK UI custom configuration](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/web-sdk-ui-custom-configuration-description).
        self.ui_custom_url = ui_custom_url
        # The custom user ID in the customer business. Make sure that the ID is unique.
        self.user_id = user_id
        # The expiration date of the ID document.
        # 
        # This parameter is required when the **CertType** parameter is set to **PASSPORT** and the **Mode** parameter is set to **3**.
        self.validity_date = validity_date
        # Specifies whether to enable video evidence. Valid values:
        # 
        # - **true**: Enables video evidence.
        # 
        # - **false**: Does not enable video evidence. This is the default value.
        # 
        # > Because video files are large, the system discards video files to prioritize the transmission of necessary authentication images when the network is unstable. We recommend that you set your business to weakly depend on videos.
        self.video_evidence = video_evidence
        # The custom willingness content. This parameter is required when personalized settings are enabled. The value is a JSON string of a string list.
        # 
        # - In the read-along scenario: The content cannot exceed 60 Chinese characters (excluding punctuation marks), and the list contains only one element.
        # 
        # - In the Q&A scenario: You can configure up to three questions. Each question cannot exceed 30 Chinese characters, and each question is an element in the list.
        self.voluntary_customized_content = voluntary_customized_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_quality_check is not None:
            result['AppQualityCheck'] = self.app_quality_check

        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        if self.birthday is not None:
            result['Birthday'] = self.birthday

        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.camera_selection is not None:
            result['CameraSelection'] = self.camera_selection

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_no is not None:
            result['CertNo'] = self.cert_no

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.certify_url_style is not None:
            result['CertifyUrlStyle'] = self.certify_url_style

        if self.certify_url_type is not None:
            result['CertifyUrlType'] = self.certify_url_type

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.enable_album_upload is not None:
            result['EnableAlbumUpload'] = self.enable_album_upload

        if self.enable_beauty is not None:
            result['EnableBeauty'] = self.enable_beauty

        if self.enable_tts is not None:
            result['EnableTts'] = self.enable_tts

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.face_contrast_picture is not None:
            result['FaceContrastPicture'] = self.face_contrast_picture

        if self.face_contrast_picture_url is not None:
            result['FaceContrastPictureUrl'] = self.face_contrast_picture_url

        if self.face_guard_output is not None:
            result['FaceGuardOutput'] = self.face_guard_output

        if self.h_5degrade_confirm_btn is not None:
            result['H5DegradeConfirmBtn'] = self.h_5degrade_confirm_btn

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.model is not None:
            result['Model'] = self.model

        if self.need_multi_face_check is not None:
            result['NeedMultiFaceCheck'] = self.need_multi_face_check

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name

        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no

        if self.procedure_priority is not None:
            result['ProcedurePriority'] = self.procedure_priority

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.rarely_characters is not None:
            result['RarelyCharacters'] = self.rarely_characters

        if self.read_img is not None:
            result['ReadImg'] = self.read_img

        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.suitable_type is not None:
            result['SuitableType'] = self.suitable_type

        if self.ui_custom_url is not None:
            result['UiCustomUrl'] = self.ui_custom_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.validity_date is not None:
            result['ValidityDate'] = self.validity_date

        if self.video_evidence is not None:
            result['VideoEvidence'] = self.video_evidence

        if self.voluntary_customized_content is not None:
            result['VoluntaryCustomizedContent'] = self.voluntary_customized_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppQualityCheck') is not None:
            self.app_quality_check = m.get('AppQualityCheck')

        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')

        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('CameraSelection') is not None:
            self.camera_selection = m.get('CameraSelection')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('CertifyUrlStyle') is not None:
            self.certify_url_style = m.get('CertifyUrlStyle')

        if m.get('CertifyUrlType') is not None:
            self.certify_url_type = m.get('CertifyUrlType')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('EnableAlbumUpload') is not None:
            self.enable_album_upload = m.get('EnableAlbumUpload')

        if m.get('EnableBeauty') is not None:
            self.enable_beauty = m.get('EnableBeauty')

        if m.get('EnableTts') is not None:
            self.enable_tts = m.get('EnableTts')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('FaceContrastPicture') is not None:
            self.face_contrast_picture = m.get('FaceContrastPicture')

        if m.get('FaceContrastPictureUrl') is not None:
            self.face_contrast_picture_url = m.get('FaceContrastPictureUrl')

        if m.get('FaceGuardOutput') is not None:
            self.face_guard_output = m.get('FaceGuardOutput')

        if m.get('H5DegradeConfirmBtn') is not None:
            self.h_5degrade_confirm_btn = m.get('H5DegradeConfirmBtn')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NeedMultiFaceCheck') is not None:
            self.need_multi_face_check = m.get('NeedMultiFaceCheck')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')

        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')

        if m.get('ProcedurePriority') is not None:
            self.procedure_priority = m.get('ProcedurePriority')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RarelyCharacters') is not None:
            self.rarely_characters = m.get('RarelyCharacters')

        if m.get('ReadImg') is not None:
            self.read_img = m.get('ReadImg')

        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SuitableType') is not None:
            self.suitable_type = m.get('SuitableType')

        if m.get('UiCustomUrl') is not None:
            self.ui_custom_url = m.get('UiCustomUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('ValidityDate') is not None:
            self.validity_date = m.get('ValidityDate')

        if m.get('VideoEvidence') is not None:
            self.video_evidence = m.get('VideoEvidence')

        if m.get('VoluntaryCustomizedContent') is not None:
            self.voluntary_customized_content = m.get('VoluntaryCustomizedContent')

        return self

