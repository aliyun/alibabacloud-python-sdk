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
        model: str = None,
        ocr: str = None,
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
        use_nfc: str = None,
        verify_model: str = None,
    ):
        # <warning>This feature is currently not supported by **Web SDK**. Please refer to the App SDK integration if needed.</warning>
        # 
        # Whether to enable strict face quality detection:
        # - Y: Enable (default)
        # - N: Disable
        self.app_quality_check = app_quality_check
        # Whether to enable authoritative identity verification, currently applicable only to the second-generation ID card in mainland China. (IDV product input parameter)
        self.authorize = authorize
        # Whether to enable automatic registration
        self.auto_registration = auto_registration
        # Security Token, used for preventing duplication and tampering. If this parameter is passed, the CallbackToken field will be displayed in the callback address.
        self.callback_token = callback_token
        # Callback notification address for authentication results. The default callback request method is GET, and the callback address must start with https. After completing the authentication, the platform will call back this address and automatically add the transactionId, passed, and subcode fields.
        self.callback_url = callback_url
        # Whether to enable adaptive color-changing window border
        # - **Y**: Enable
        # - **N**: Disable
        self.chameleon_frame_enable = chameleon_frame_enable
        # Whether to crop. (IDV product input parameter)
        self.crop = crop
        # Date of birth on the document
        # 
        # **MRTDInput = 2** is required.
        self.date_of_birth = date_of_birth
        # Expiration date on the document
        # 
        # **MRTDInput = 2** is required.
        self.date_of_expiry = date_of_expiry
        # User\\"s real name.
        self.doc_name = doc_name
        # User\\"s document number.
        self.doc_no = doc_no
        # Customer-defined input to specify whether to collect more pages
        self.doc_page_config = doc_page_config
        # Document capture mode.
        # 
        # - manual: Manual capture.
        # - auto: Automatic capture (default)
        self.doc_scan_mode = doc_scan_mode
        # Document type, uniquely identified by an 8-digit combination.
        # Note: This parameter is required only when ProductCode is KYC_GLOBAL, OCR_GLOBAL, or IDR_GLOBAL.
        self.doc_type = doc_type
        # Whether to require a video for evidence.
        # 
        # - N: Not required (default).
        # 
        # - Y: During the authentication process, a 1~2 second video of the user\\"s face will be captured and returned via the query interface.
        # 
        # > Due to the large size of the video file, the system may discard it when the network is unstable, prioritizing the transmission of necessary images for authentication.
        self.doc_video = doc_video
        # Document number
        # 
        # **MRTDInput = 2** is required.
        self.document_number = document_number
        # In the document OCR recognition step, whether the recognition result page is editable:
        # 
        # - **0**: Not editable
        # 
        # - **1** (default): Editable
        self.edit_ocr_result = edit_ocr_result
        # Experience code
        self.experience_code = experience_code
        # Face library to be compared
        self.face_group_codes = face_group_codes
        # Base64 encoded face image. If you choose to pass the face image via FacePictureBase64, please check the image size and do not upload images larger than 1 MB.
        # When productCode is FV_GLOBAL, choose one of the parameters between FacePictureBase64 and FacePictureUrl to pass in.
        self.face_picture_base_64 = face_picture_base_64
        # Face image URL. A publicly accessible HTTP or HTTPS link. When productCode is FV_GLOBAL, choose one of the parameters between FacePictureUrl and FacePictureBase to pass in.
        self.face_picture_url = face_picture_url
        # Face library for registration.
        self.face_register_group_code = face_register_group_code
        # Face verification threshold
        self.face_verify_threshold = face_verify_threshold
        # Face image quality. (IDV product input parameter)
        self.id_face_quality = id_face_quality
        # Whether to enable certificate anti-counterfeiting detection. (IDV product input parameter)
        self.id_spoof = id_spoof
        # Custom OCR quality detection threshold mode:
        # - **0**: Standard mode
        # - **1**: Strict mode
        # - **2**: Lenient mode
        # - **3** (default): Disable quality detection
        self.id_threshold = id_threshold
        # Language configuration. (IDV product input parameter)
        self.language_config = language_config
        # Source of MRTD verification parameters. This parameter is required to decrypt information when reading the document chip via NFC.
        # 
        # - **0**: User input
        # 
        # - **1**: OCR read
        # 
        # - **2**: Passed through the API
        self.mrtdinput = mrtdinput
        # A unique business identifier defined by the merchant, used for subsequent troubleshooting. It supports a combination of letters and numbers, with a maximum length of 32 characters. Please ensure its uniqueness.
        self.merchant_biz_id = merchant_biz_id
        # Your custom user ID or other identifiers that can recognize specific users, such as phone numbers or email addresses. It is strongly recommended to pre-desensitize the value of this field, for example, by hashing it.
        self.merchant_user_id = merchant_user_id
        # Metainfo environment parameter, which needs to be obtained through the client SDK.
        self.meta_info = meta_info
        # The type of liveness detection to be performed:
        # 
        # - **LIVENESS** (default): Blinking action liveness detection.
        # 
        # - **PHOTINUS_LIVENESS**: Blinking action liveness + photinus liveness dual detection.
        # 
        # > 
        # > - For supported SDK versions, see [SDK Publishing Record](https://www.alibabacloud.com/help/zh/ekyc/latest/sdk-publishing-record?spm=a2c63.p38356.0.i99).
        # > - PC does not support photinus liveness dual detection.
        self.model = model
        # Whether to enable OCR. (IDV product input parameter)
        self.ocr = ocr
        # Page configuration for collection, multiple pages are connected using commas. The value range is as follows:
        # - **01**: Front side of the document
        # 
        # - **01,02**: Front and back sides of the document
        # 
        # > When this value is 01,02, currently only Chinese and Vietnamese IDs are supported.
        self.pages = pages
        # When compatibility issues occur with H5-based mobile authentication, whether to allow a fallback handling method.
        # 
        # - **url** (default): Support fallback. The page displays the authentication URL, which users can copy and open in another browser to continue the authentication process.
        # 
        # - **keep**: Do not support fallback. Directly return the error reason and end the authentication process.
        # 
        # 
        # > 
        # > - This switch is not supported on PC.
        # > - If the business scenario involves completing authentication through an embedded web page in an app, it is recommended to set this parameter to `keep` to disallow URL fallback.
        self.procedure_priority = procedure_priority
        # The product solution to be integrated. The values are as follows:
        # 
        # - KYC_GLOBAL (eKYC product solution)
        # - FV_GLOBAL (Live Face Verification)
        # - FL_GLOBAL (Liveness Detection)
        # - IDR_GLOBAL (Single Document Verification)
        # - OCR_GLOBAL (Single Document OCR)
        self.product_code = product_code
        # Supports card and face sequential arrangement:
        # 
        # - DOC_FACE (default)
        # - FACE_DOC
        # 
        # Note: This parameter is required only when ProductCode is KYC_GLOBAL.
        self.product_flow = product_flow
        # Number of duplicate faces returned
        self.return_faces = return_faces
        # Client-side callback address.
        self.return_url = return_url
        # Whether to save the face image
        self.save_face_picture = save_face_picture
        # Scene code. (IDV product input parameter)
        self.scene_code = scene_code
        # Represents different security levels in the authentication process. The available values are as follows:
        # 
        # 01: Normal mode (default).
        # 02: Secure mode, a relatively strict mode, suitable for high-risk scenarios. (IDV product input parameter)
        self.security_level = security_level
        # In the document OCR recognition step, whether to display the album upload entry:
        # 
        # - **1**: Display (default)
        # 
        # - **0**: Do not display
        self.show_album_icon = show_album_icon
        # Switch to control whether to display the guide page:
        # 
        # - **1**: Display (default)
        # 
        # - **0**: Do not display
        self.show_guide_page = show_guide_page
        # In the document OCR recognition step, whether to display the recognition result page:
        # 
        # - **1**: Display (default)
        # 
        # - **0**: Do not display
        self.show_ocr_result = show_ocr_result
        # Custom UI configuration. Based on the configuration template, convert your custom UI configuration into a JSON string and pass it through this interface. For more information, see [IDV UI Customization](https://www.alibabacloud.com/help/zh/ekyc/latest/idv-kyc-custom-skin?spm=a2c63.p38356.0.i60).
        self.style_config = style_config
        # Base64 encoding of the portrait photo.
        self.target_face_picture = target_face_picture
        # Portrait image URL, accessible via public HTTP or HTTPS link.
        self.target_face_picture_url = target_face_picture_url
        # When **DocType**=01000000 (global passport), you can choose whether to enable NFC verification.
        # - **Y** (enable)
        # - **N** (disable)
        self.use_nfc = use_nfc
        # Type of verification
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

        if self.model is not None:
            result['Model'] = self.model

        if self.ocr is not None:
            result['Ocr'] = self.ocr

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

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')

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

        if m.get('UseNFC') is not None:
            self.use_nfc = m.get('UseNFC')

        if m.get('VerifyModel') is not None:
            self.verify_model = m.get('VerifyModel')

        return self

