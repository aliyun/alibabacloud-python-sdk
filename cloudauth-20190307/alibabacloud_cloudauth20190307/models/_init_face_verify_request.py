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
        enable_beauty: str = None,
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
        # Specifies whether the SDK enables strict face quality detection:
        # 
        # - **Y**: enabled.
        # 
        # - **N**: disabled (default).
        # 
        # 
        # > 
        # > - If this parameter is enabled, the SDK must integrate the [strict face quality detection module](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/description-of-sdk-package-clipping). Strict quality detection may reduce the face authentication success rate.
        # > - Only Android SDK 2.3.24 and later versions are supported.
        self.app_quality_check = app_quality_check
        # The user authorization ID. Maximum length: 64 characters.
        self.auth_id = auth_id
        # The date of birth on the certificate.
        # 
        # This field is required when **CertType** is set to **PASSPORT** and **Mode** is set to **3**.
        self.birthday = birthday
        # The security token that you generate to prevent duplication and tampering.
        # 
        # If this value is set, the **CallbackToken** field is displayed in the callback URL.
        self.callback_token = callback_token
        # The callback URL for the authentication result. The callback request method is GET by default, and the callback URL must start with `https`. After authentication is complete, the platform calls back this URL and automatically appends the `certifyId` and `passed` fields. The `passed` field returns the subcode value. Example: `https://www.alibabacloud.com?callbackToken=1000004826&certifyId=shaxxxx&passed=200.`
        # 
        # <notice>
        # 
        # - The callback is triggered only when authentication is complete (including both passed and failed). If the user abandons authentication, an abnormal break occurs, or authentication is not performed, no notification is sent. After receiving the callback notification, invoke the query operation to obtain authentication details if needed.
        # - The URL is validated for public network access before the operation is invoked. If the URL is not accessible over the public network, a 401 error is returned.
        # - After receiving the callback, return HTTP status code 200. Otherwise, a retry is triggered with two callbacks within 3 seconds.
        # 
        # </notice>
        self.callback_url = callback_url
        # Specifies whether to enable the camera selection feature:
        # 
        # - **Y**: enabled.
        # 
        # - **N**: disabled (default).
        # 
        # > This feature takes effect only for PC integration mode. After this feature is enabled, users can select a camera for authentication.
        self.camera_selection = camera_selection
        # The real name.
        self.cert_name = cert_name
        # The certificate number.
        self.cert_no = cert_no
        # The certificate type.
        # Currently, only ID cards are supported. Set this parameter to IDENTITY_CARD.
        self.cert_type = cert_type
        # >Warning: This parameter will be deprecated.</warning>
        # 
        # The CertifyId from a previous successful ID Verification. The photo from that authentication is used as the comparison photo.
        # 
        # > You can use one of the following four methods to submit a photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS. Select only one method.
        self.certify_id = certify_id
        # The type of the returned **CertifyUrl**. Valid values:
        # 
        # - **L**: original long URL.
        # 
        # - **S** (default): short URL.
        self.certify_url_style = certify_url_style
        # The Web SDK device type. Valid values: **WEB** or **H5**.
        # 
        # > Only Web SDK device types are supported.
        self.certify_url_type = certify_url_type
        # Specifies whether to allow cropping of the face photo. By default, cropping is not allowed.
        # 
        # - T: allows cropping.
        # 
        # - F: does not allow cropping.
        # 
        # > If the requested image is not captured by a standard liveness detection SDK, allow cropping of the face photo. After this feature is enabled, the requested image is cropped and corrected before the request is sent to the service.
        self.crop = crop
        self.enable_beauty = enable_beauty
        # The encryption algorithm. Currently, only the SM2 algorithm is supported.
        # 
        # After encrypted transmission is enabled, pass in the encrypted CertName and CertNo. For more information about encryption, refer to [Parameter encryption description](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/description-of-parameter-encryption#task-2229332).
        self.encrypt_type = encrypt_type
        # The Base64-encoded photo.
        # 
        # > You can use one of the following four methods to submit a photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS. Select only one method.
        self.face_contrast_picture = face_contrast_picture
        # The OSS photo URL. Currently, only authorized OSS photo URLs are supported.
        # 
        # > You can use one of the following four methods to submit a photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS. Select only one method.
        self.face_contrast_picture_url = face_contrast_picture_url
        # The device assistant tag type. Valid values: **DeviceRisk**.
        # 
        # >
        # > - Selecting device assistant output incurs additional fees. For more information, refer to [Paid value-added services](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/face-guard).
        # > - If you do not need device assistant tag output, do not pass this parameter or pass an empty value.
        self.face_guard_output = face_guard_output
        # Specifies whether to display the "I have completed authentication" button on the H5 fallback page after authentication is complete:
        # - **Y**: enabled.
        # - **N** (default): disabled.
        self.h_5degrade_confirm_btn = h_5degrade_confirm_btn
        # The IP address of the user.
        self.ip = ip
        # The Metainfo environment parameter, which must be obtained through the client SDK.
        self.meta_info = meta_info
        # The mobile phone number of the user.
        self.mobile = mobile
        # The method for obtaining passport NFC verification elements:
        # 
        # - **1**: user input. The end user manually enters certificate element information using the UI provided by the Alibaba Cloud SDK.
        # 
        # - **3**: external parameter input. Certificate element information is passed in externally.
        # 
        # > To decode the encrypted information on the passport chip through NFC, three passport elements are required: name, date of birth, and certificate expiration date.
        self.mode = mode
        # The liveness detection type. Valid values:
        # > The liveness detection type supports only the following values. Custom actions or combinations are not supported.
        # 
        # Note:
        # The liveness detection type supports only the following values. Custom actions or combinations are not supported.
        # 
        # - **LIVENESS** (default): blink
        # 
        # - **PHOTINUS_LIVENESS**: blink + colorful light
        # 
        # - **MULTI_ACTION**: blink + head shake (the order of blink and head shake is random)
        # 
        # - **MOVE_ACTION** (recommended): move closer/farther + blink
        # 
        # - **MOVE_PHOTINUS**: move closer/farther + colorful light
        # 
        # > 
        # >- **The default liveness detection type** is supported in the following versions:
        # >   - Android SDK 1.2.6 and later
        # >   - iOS SDK 1.2.4 and later
        # >   - Harmony SDK 1.0.0 and later
        # >- Other types are supported in the latest Android/iOS/Harmony SDK versions. Integrate the latest version.
        self.model = model
        # Specifies whether to block authentication when multiple faces are detected on the device. Valid values:
        # 
        # - **Y**: blocked. The client prompts the user to redo face authentication.
        # 
        # - **N** (default): not blocked. The largest face in the frame is sent to the server for security detection.
        self.need_multi_face_check = need_multi_face_check
        # The bucket name of the authorized OSS space.
        # 
        # > You can use one of the following four methods to submit a photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS. Select only one method.
        self.oss_bucket_name = oss_bucket_name
        # The file name in the authorized OSS space.
        # 
        # > You can use one of the following four methods to submit a photo: FaceContrastPicture, FaceContrastPictureUrl, CertifyId, or OSS. Select only one method.
        self.oss_object_name = oss_object_name
        # The unique identifier of the merchant request.
        # 
        # The value is a 32-character alphanumeric string. The first few characters are a custom abbreviation defined by the merchant, the middle part can be a time segment, and the last part can be a random or incremental sequence.
        self.outer_order_no = outer_order_no
        # The fallback configuration when WebRTC or WebAssembly is incompatible during mobile H5 authentication.
        # 
        # - **keep**: fallback is not supported. The system returns directly.
        # 
        # - **url** (default): fallback is supported. An authentication URL is returned. The user opens or switches to a browser to authenticate using this URL.
        # 
        # - **video**: fallback is supported. The system camera records a 3 to 5 second blink video for authentication.
        # 
        # 
        # > 
        # > When the fallback mode is Video, the following features are disabled and product security is reduced. Configure this mode only for security scenarios.
        # > - The liveness detection type setting does not take effect.
        # > - The VideoEvidence feature is not supported.
        self.procedure_priority = procedure_priority
        # A fixed value. This parameter varies depending on the product plan:
        # - APP authentication plan: set to ID_PRO.
        # - Face liveness verification plan: set to PV_FV.
        # - Liveness detection plan: set to LR_FR.
        self.product_code = product_code
        # Specifies whether to enable the rare character mode:
        # 
        # - **Y**: enabled. An information input box is displayed before authentication. The user must enter the name with rare characters and the ID card number, and agree to the protocol before starting the authentication process.
        # 
        # - **N**: disabled (default).
        self.rarely_characters = rarely_characters
        # Specifies whether to read the certificate photo:
        # 
        # - **Y**: read.
        # 
        # - **N**: do not read.
        # 
        # > If the certificate face photo is needed in subsequent authentication steps, set this parameter to Y.
        self.read_img = read_img
        # The redirect URL for the merchant business page.
        self.return_url = return_url
        # The authentication scenario ID.
        self.scene_id = scene_id
        # The elderly-friendly configuration parameter. This parameter takes effect for each authentication request. You can select different parameters for each authentication request based on the business attributes, customer distribution, and operational characteristics of your app. Valid values (default: 0):
        # 
        # - **0**: disabled. The elderly-friendly mode is not enabled for the current authentication request.
        # 
        # - **1**: enabled. The elderly-friendly mode is enabled for the current authentication request.
        # 
        # - **2**: user choice.
        # 
        # 
        # Allows the end user to select the authentication mode. The product guide page provides two authentication entries: "Start Authentication" and "Elderly Authentication Mode". When the user selects "Elderly Authentication Mode", the system enters elderly-friendly mode.
        # > 
        # > - The elderly-friendly parameter takes effect only when the liveness detection type **Model** is set to **LIVENESS** or **MULTI_ACTION**.
        self.suitable_type = suitable_type
        # The UI configuration file URL.
        # 
        # You can view the complete configuration in [Web SDK UI custom configuration](https://www.alibabacloud.com/help/en/id-verification/financial-grade-id-verification/web-sdk-ui-custom-configuration-description).
        self.ui_custom_url = ui_custom_url
        # The custom user ID defined by the business. Keep this value unique.
        self.user_id = user_id
        # The certificate expiration date.
        # 
        # This field is required when **CertType** is set to **PASSPORT** and **Mode** is set to **3**.
        self.validity_date = validity_date
        # Specifies whether to enable video evidence:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled (default).
        # 
        # > Because video files are large, the system discards video files to prioritize the transmission of essential authentication images when the network is unstable. Set video as a weak dependency in your business logic.
        self.video_evidence = video_evidence
        # The custom voluntary content. This parameter is required when personalized settings are enabled. The format is a JSON string of a String List.
        # 
        # - For read-aloud scenarios: the content cannot exceed 60 Chinese characters (excluding punctuation), and the List contains only 1 element.
        # 
        # - For Q&A scenarios: a maximum of 3 questions can be set. Each question cannot exceed 30 Chinese characters, and each question is a separate element in the List.
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

        if self.enable_beauty is not None:
            result['EnableBeauty'] = self.enable_beauty

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

        if m.get('EnableBeauty') is not None:
            self.enable_beauty = m.get('EnableBeauty')

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

