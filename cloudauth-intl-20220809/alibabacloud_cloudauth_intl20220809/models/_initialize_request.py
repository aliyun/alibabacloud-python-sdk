# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class InitializeRequest(DaraModel):
    def __init__(
        self,
        app_quality_check: str = None,
        authorize: str = None,
        auto_registration: str = None,
        callback_token: str = None,
        callback_url: str = None,
        chameleon_frame_enable: str = None,
        crop: str = None,
        date_of_birth: str = None,
        date_of_expiry: str = None,
        doc_name: str = None,
        doc_no: str = None,
        doc_page_config: List[str] = None,
        doc_scan_mode: str = None,
        doc_type: str = None,
        doc_video: str = None,
        document_number: str = None,
        edit_ocr_result: str = None,
        email: str = None,
        experience_code: str = None,
        face_group_codes: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        face_register_group_code: str = None,
        face_verify_threshold: str = None,
        id_face_quality: str = None,
        id_spoof: str = None,
        id_threshold: str = None,
        language_config: str = None,
        mrtdinput: str = None,
        merchant_biz_id: str = None,
        merchant_user_id: str = None,
        meta_info: str = None,
        mobile: str = None,
        model: str = None,
        ocr: str = None,
        ocr_value_standard: str = None,
        pages: str = None,
        procedure_priority: str = None,
        product_code: str = None,
        product_flow: str = None,
        return_faces: str = None,
        return_url: str = None,
        save_face_picture: str = None,
        scene_code: str = None,
        security_level: str = None,
        show_album_icon: str = None,
        show_guide_page: str = None,
        show_ocr_result: str = None,
        style_config: str = None,
        target_face_picture: str = None,
        target_face_picture_url: str = None,
        template_config: str = None,
        template_ran_count: str = None,
        template_type: str = None,
        use_nfc: str = None,
        verify_model: str = None,
    ):
        # <warning>This feature is **not supported by the Web SDK**. To use this feature, integrate the App SDK.</warning>
        # 
        # Specifies whether to enable strict face quality detection:
        # - Y: enabled (default)
        # - N: disabled.
        self.app_quality_check = app_quality_check
        # Specifies whether to enable authoritative identity verification. Currently, this applies only to second-generation ID cards in the Chinese mainland. This is an input parameter for the IDV product.
        self.authorize = authorize
        # Specifies whether to enable auto-registration.
        self.auto_registration = auto_registration
        # The security token used for anti-replay and anti-tampering verification. If this parameter is specified, the CallbackToken field is included in the callback URL.
        self.callback_token = callback_token
        # The callback URL for the authentication result. The callback request method is GET by default. The callback URL must start with https. After the authentication is complete, the platform calls back this URL and automatically appends the transactionId, passed, and subcode fields.
        self.callback_url = callback_url
        # Specifies whether to enable the adaptive color-changing window frame.
        # - **Y**: enabled
        # - **N**: disabled.
        self.chameleon_frame_enable = chameleon_frame_enable
        # Specifies whether to enable cropping. This is an input parameter for the IDV product.
        self.crop = crop
        # The date of birth on the document.
        # 
        # Required when **MRTDInput = 2**.
        self.date_of_birth = date_of_birth
        # The expiration date on the document.
        # 
        # Required when **MRTDInput** = 2.
        self.date_of_expiry = date_of_expiry
        # The real name of the user.
        self.doc_name = doc_name
        # The document number of the user.
        self.doc_no = doc_no
        # The custom configuration for whether to capture additional pages.
        self.doc_page_config = doc_page_config
        # The document capture photo mode.
        # 
        # - manual: manual photo capture.
        # - auto: automatic photo capture (default).
        self.doc_scan_mode = doc_scan_mode
        # The document type.
        # >For the eKYC_PRO and ID_OCR_MAX solutions, see the official documentation: https://www.alibabacloud.com/help/zh/ekyc/latest/certificate-code-table?spm=a2c63.p38356.help-menu-445633.d_2_8_2_0.279147abwKAWbr
        # 
        # >For the ID_OCR, eKYC, and eKYC_MIN solutions, see the document type list in the official documentation: https://www.alibabacloud.com/help/zh/ekyc/latest/gnhekqy05ni51m4c?spm=a2c63.p38356.help-menu-445633.d_2_3_1_0_0_0.6243244777KoZ7.
        self.doc_type = doc_type
        # Specifies whether to save an evidence video.
        # 
        # - N: not required (default).
        # 
        # - Y: a face verification video (1 to 2 seconds) is captured during the authentication process and returned through the query API.
        # 
        # > Because video files are large, the system discards the video file when the network is unstable to prioritize the transmission of images required for authentication.
        self.doc_video = doc_video
        # The document number.
        # 
        # Required when **MRTDInput = 2**.
        self.document_number = document_number
        # Specifies whether the recognition result page is editable during the document OCR recognition step:
        # 
        # - **0**: not editable
        # 
        # - **1** (default): editable.
        self.edit_ocr_result = edit_ocr_result
        # The Indonesian email address. This field takes effect only when Authorize is set to T.
        # 
        # > 
        # > - This field is required only when the Indonesian data source is enabled.
        self.email = email
        # The experience code.
        self.experience_code = experience_code
        # The face libraries for comparison.
        self.face_group_codes = face_group_codes
        # The Base64-encoded face photo. If you use FacePictureBase64 to pass in the face photo, check the photo size and do not pass in an excessively large photo.
        self.face_picture_base_64 = face_picture_base_64
        # The URL of the face photo. The URL must be a publicly accessible HTTP or HTTPS link.
        self.face_picture_url = face_picture_url
        # The face registration library.
        self.face_register_group_code = face_register_group_code
        # The face verification threshold.
        self.face_verify_threshold = face_verify_threshold
        # The face image quality. This is an input parameter for the IDV product.
        self.id_face_quality = id_face_quality
        # Specifies whether to enable document anti-spoofing detection. This is an input parameter for the IDV product.
        self.id_spoof = id_spoof
        # The custom OCR quality detection threshold mode:
        # - **0**: standard mode
        # - **1**: strict mode
        # - **2**: loose mode
        # - **3** (default): quality detection disabled.
        self.id_threshold = id_threshold
        # The language configuration. This is an input parameter for the IDV product.
        self.language_config = language_config
        # The input source for MRTD verification parameters. This parameter is required for decrypting information when reading document chip data via NFC.
        # 
        # - **0**: user input
        # 
        # - **1**: OCR reading
        # 
        # - **2**: API input.
        self.mrtdinput = mrtdinput
        # The merchant-defined unique business ID used for subsequent troubleshooting. The value can contain letters and digits with a maximum length of 32 characters. Make sure the value is unique.
        self.merchant_biz_id = merchant_biz_id
        # Your custom user ID or another identifier that can identify a specific user, such as a phone number or email address. We strongly recommend that you desensitize this field value in advance, such as by hashing the value.
        self.merchant_user_id = merchant_user_id
        # The MetaInfo environment parameter. Obtain this value by using the client SDK.
        self.meta_info = meta_info
        # The Indonesian phone number. The format must start with +62 followed by 9 to 11 digits. This field takes effect only when Authorize is set to T.
        # 
        # > 
        # > - This field is required only when the Indonesian data source is enabled.
        self.mobile = mobile
        # The type of liveness detection:
        # 
        # - **LIVENESS** (default): blink action liveness detection.
        # 
        # - **PHOTINUS_LIVENESS**: blink action liveness + colorful liveness dual detection.
        # 
        # > 
        # > - For supported SDK versions, see [SDK release notes](https://www.alibabacloud.com/help/zh/ekyc/latest/sdk-publishing-record?spm=a2c63.p38356.0.i99).
        # > - Colorful liveness dual detection is not supported on PC.
        self.model = model
        # Specifies whether to enable OCR. This is an input parameter for the IDV product.
        self.ocr = ocr
        # Specifies whether to return additional OCR recognition standardized format fields:
        # 
        # 0: no (default)
        # 
        # 1: yes.
        self.ocr_value_standard = ocr_value_standard
        # The capture page configuration. Use commas (,) to connect multiple pages. Valid values:
        # - **01**: portrait side of the document
        # 
        # - **01,02**: portrait side and back side of the document
        # 
        # > When this value is set to 01,02, only Chinese ID cards and Vietnamese ID cards are supported.
        self.pages = pages
        # Specifies whether to allow a degraded processing method when compatibility issues occur during mobile H5 authentication.
        # 
        # - **url (default)**: degradation supported. The page displays the authentication URL, and the user can copy the URL or switch browsers to continue authentication.
        # 
        # - **keep**: degradation not supported. The error reason is returned directly and the authentication flow ends.
        # 
        # 
        # > 
        # > - This switch is not supported on PC.
        # > - If the business scenario involves completing authentication within an in-app embedded web page, set this parameter to keep to disallow URL degradation.
        self.procedure_priority = procedure_priority
        # The product solution to use.
        # >For more information, see the official documentation: https://www.alibabacloud.com/help/zh/ekyc/latest/product-introduction?spm=a2c63.p38356.0.i1.
        self.product_code = product_code
        # The order of document and face capture:
        # 
        # - DOC_FACE (default)
        # - FACE_DOC
        # 
        # Note: This parameter is required only when ProductCode is set to KYC_GLOBAL.
        self.product_flow = product_flow
        # The number of duplicate faces returned.
        self.return_faces = return_faces
        # The client-side callback URL.
        self.return_url = return_url
        # Specifies whether to save the face picture.
        self.save_face_picture = save_face_picture
        # The scene code. This is an input parameter for the IDV product.
        self.scene_code = scene_code
        # The pattern that represents different security levels of the authentication flow. Valid values:
        # 
        # 01: normal pattern (default).
        # 02: safe mode, a relatively strict pattern that is active for high-risk scenarios. This is an input parameter for the IDV product.
        self.security_level = security_level
        # Specifies whether to display the album upload entry during the document OCR recognition step:
        # 
        # - **1**: display (default)
        # 
        # - **0**: do not display.
        self.show_album_icon = show_album_icon
        # Specifies whether to display the guide page:
        # 
        # - **1**: display (default)
        # 
        # - **0**: do not display.
        self.show_guide_page = show_guide_page
        # Specifies whether to display the recognition result page during the document OCR recognition step:
        # 
        # - **1**: display (default)
        # 
        # - **0**: do not display.
        self.show_ocr_result = show_ocr_result
        # The custom UI configuration. Convert your custom UI configuration to a JSON string based on the configuration template and pass it in through this parameter. For more information, see [IDV UI style customization](https://www.alibabacloud.com/help/zh/ekyc/latest/idv-kyc-custom-skin?spm=a2c63.p38356.0.i60).
        self.style_config = style_config
        # The Base64-encoded portrait photo.
        self.target_face_picture = target_face_picture
        # The URL of the portrait image. The URL must be a publicly accessible HTTP or HTTPS link.
        self.target_face_picture_url = target_face_picture_url
        # The custom action pool configuration for liveness detection.
        # This parameter is required when Model is set to TEMPLATE.
        # Configuration rule: separate multiple action codes with commas (,). Best practices: include at least one frontal face action (such as blink) and no more than 3 actions in total.
        # Action lookup table:
        # 
        # - Blink: 01
        # - Open Mouth: 02
        # - Shake Head Left: 03
        # - Shake Head Right: 04
        # - Move Farther: 05
        # - Move Closer: 06
        # - Photinus: 07.
        self.template_config = template_config
        # The number of actions randomly selected from TemplateConfig.
        # This parameter takes effect only when TemplateType is set to Ran.
        # 
        # - Validation rules:
        # - The value must be greater than 1. The value must be less than or equal to the total number of actions configured in TemplateConfig. If not specified, the default value equals the total number of actions in TemplateConfig.
        self.template_ran_count = template_ran_count
        # The execution order of liveness detection actions in TemplateConfig.
        # This parameter is required when Model is set to TEMPLATE.
        # 
        # - Seq: actions are executed in the order configured in TemplateConfig from left to right.
        # - Ran: actions are executed in random order. When this option is selected, TemplateConfig must contain more than one action.
        self.template_type = template_type
        # Specifies whether to enable NFC verification when **DocType** is set to 01000000 (global passport).
        # - **Y**: enabled
        # - **N**: disabled.
        self.use_nfc = use_nfc
        # The verification type.
        self.verify_model = verify_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_quality_check is not None:
            result['AppQualityCheck'] = self.app_quality_check

        if self.authorize is not None:
            result['Authorize'] = self.authorize

        if self.auto_registration is not None:
            result['AutoRegistration'] = self.auto_registration

        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token

        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url

        if self.chameleon_frame_enable is not None:
            result['ChameleonFrameEnable'] = self.chameleon_frame_enable

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.date_of_birth is not None:
            result['DateOfBirth'] = self.date_of_birth

        if self.date_of_expiry is not None:
            result['DateOfExpiry'] = self.date_of_expiry

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.doc_no is not None:
            result['DocNo'] = self.doc_no

        if self.doc_page_config is not None:
            result['DocPageConfig'] = self.doc_page_config

        if self.doc_scan_mode is not None:
            result['DocScanMode'] = self.doc_scan_mode

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        if self.doc_video is not None:
            result['DocVideo'] = self.doc_video

        if self.document_number is not None:
            result['DocumentNumber'] = self.document_number

        if self.edit_ocr_result is not None:
            result['EditOcrResult'] = self.edit_ocr_result

        if self.email is not None:
            result['Email'] = self.email

        if self.experience_code is not None:
            result['ExperienceCode'] = self.experience_code

        if self.face_group_codes is not None:
            result['FaceGroupCodes'] = self.face_group_codes

        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64

        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url

        if self.face_register_group_code is not None:
            result['FaceRegisterGroupCode'] = self.face_register_group_code

        if self.face_verify_threshold is not None:
            result['FaceVerifyThreshold'] = self.face_verify_threshold

        if self.id_face_quality is not None:
            result['IdFaceQuality'] = self.id_face_quality

        if self.id_spoof is not None:
            result['IdSpoof'] = self.id_spoof

        if self.id_threshold is not None:
            result['IdThreshold'] = self.id_threshold

        if self.language_config is not None:
            result['LanguageConfig'] = self.language_config

        if self.mrtdinput is not None:
            result['MRTDInput'] = self.mrtdinput

        if self.merchant_biz_id is not None:
            result['MerchantBizId'] = self.merchant_biz_id

        if self.merchant_user_id is not None:
            result['MerchantUserId'] = self.merchant_user_id

        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.model is not None:
            result['Model'] = self.model

        if self.ocr is not None:
            result['Ocr'] = self.ocr

        if self.ocr_value_standard is not None:
            result['OcrValueStandard'] = self.ocr_value_standard

        if self.pages is not None:
            result['Pages'] = self.pages

        if self.procedure_priority is not None:
            result['ProcedurePriority'] = self.procedure_priority

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_flow is not None:
            result['ProductFlow'] = self.product_flow

        if self.return_faces is not None:
            result['ReturnFaces'] = self.return_faces

        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url

        if self.save_face_picture is not None:
            result['SaveFacePicture'] = self.save_face_picture

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.show_album_icon is not None:
            result['ShowAlbumIcon'] = self.show_album_icon

        if self.show_guide_page is not None:
            result['ShowGuidePage'] = self.show_guide_page

        if self.show_ocr_result is not None:
            result['ShowOcrResult'] = self.show_ocr_result

        if self.style_config is not None:
            result['StyleConfig'] = self.style_config

        if self.target_face_picture is not None:
            result['TargetFacePicture'] = self.target_face_picture

        if self.target_face_picture_url is not None:
            result['TargetFacePictureUrl'] = self.target_face_picture_url

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_ran_count is not None:
            result['TemplateRanCount'] = self.template_ran_count

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.use_nfc is not None:
            result['UseNFC'] = self.use_nfc

        if self.verify_model is not None:
            result['VerifyModel'] = self.verify_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppQualityCheck') is not None:
            self.app_quality_check = m.get('AppQualityCheck')

        if m.get('Authorize') is not None:
            self.authorize = m.get('Authorize')

        if m.get('AutoRegistration') is not None:
            self.auto_registration = m.get('AutoRegistration')

        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')

        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')

        if m.get('ChameleonFrameEnable') is not None:
            self.chameleon_frame_enable = m.get('ChameleonFrameEnable')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('DateOfBirth') is not None:
            self.date_of_birth = m.get('DateOfBirth')

        if m.get('DateOfExpiry') is not None:
            self.date_of_expiry = m.get('DateOfExpiry')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('DocNo') is not None:
            self.doc_no = m.get('DocNo')

        if m.get('DocPageConfig') is not None:
            self.doc_page_config = m.get('DocPageConfig')

        if m.get('DocScanMode') is not None:
            self.doc_scan_mode = m.get('DocScanMode')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        if m.get('DocVideo') is not None:
            self.doc_video = m.get('DocVideo')

        if m.get('DocumentNumber') is not None:
            self.document_number = m.get('DocumentNumber')

        if m.get('EditOcrResult') is not None:
            self.edit_ocr_result = m.get('EditOcrResult')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ExperienceCode') is not None:
            self.experience_code = m.get('ExperienceCode')

        if m.get('FaceGroupCodes') is not None:
            self.face_group_codes = m.get('FaceGroupCodes')

        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')

        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')

        if m.get('FaceRegisterGroupCode') is not None:
            self.face_register_group_code = m.get('FaceRegisterGroupCode')

        if m.get('FaceVerifyThreshold') is not None:
            self.face_verify_threshold = m.get('FaceVerifyThreshold')

        if m.get('IdFaceQuality') is not None:
            self.id_face_quality = m.get('IdFaceQuality')

        if m.get('IdSpoof') is not None:
            self.id_spoof = m.get('IdSpoof')

        if m.get('IdThreshold') is not None:
            self.id_threshold = m.get('IdThreshold')

        if m.get('LanguageConfig') is not None:
            self.language_config = m.get('LanguageConfig')

        if m.get('MRTDInput') is not None:
            self.mrtdinput = m.get('MRTDInput')

        if m.get('MerchantBizId') is not None:
            self.merchant_biz_id = m.get('MerchantBizId')

        if m.get('MerchantUserId') is not None:
            self.merchant_user_id = m.get('MerchantUserId')

        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')

        if m.get('OcrValueStandard') is not None:
            self.ocr_value_standard = m.get('OcrValueStandard')

        if m.get('Pages') is not None:
            self.pages = m.get('Pages')

        if m.get('ProcedurePriority') is not None:
            self.procedure_priority = m.get('ProcedurePriority')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductFlow') is not None:
            self.product_flow = m.get('ProductFlow')

        if m.get('ReturnFaces') is not None:
            self.return_faces = m.get('ReturnFaces')

        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')

        if m.get('SaveFacePicture') is not None:
            self.save_face_picture = m.get('SaveFacePicture')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('ShowAlbumIcon') is not None:
            self.show_album_icon = m.get('ShowAlbumIcon')

        if m.get('ShowGuidePage') is not None:
            self.show_guide_page = m.get('ShowGuidePage')

        if m.get('ShowOcrResult') is not None:
            self.show_ocr_result = m.get('ShowOcrResult')

        if m.get('StyleConfig') is not None:
            self.style_config = m.get('StyleConfig')

        if m.get('TargetFacePicture') is not None:
            self.target_face_picture = m.get('TargetFacePicture')

        if m.get('TargetFacePictureUrl') is not None:
            self.target_face_picture_url = m.get('TargetFacePictureUrl')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateRanCount') is not None:
            self.template_ran_count = m.get('TemplateRanCount')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('UseNFC') is not None:
            self.use_nfc = m.get('UseNFC')

        if m.get('VerifyModel') is not None:
            self.verify_model = m.get('VerifyModel')

        return self

