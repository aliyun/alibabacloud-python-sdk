# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class UpdateSmsQualificationRequest(DaraModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics: List[main_models.UpdateSmsQualificationRequestBusinessLicensePics] = None,
        bussiness_license_exp_date: str = None,
        certify_code: str = None,
        company_name: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_back_side: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_id_card_front_side: str = None,
        legal_person_name: str = None,
        order_id: int = None,
        other_files: List[main_models.UpdateSmsQualificationRequestOtherFiles] = None,
        owner_id: int = None,
        qualification_group_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Validity period of the administrator ID card. Format: YYYY-MM-DD~YYYY-MM-DD.
        # > When the certificate validity period is long-term, the end date can be set to 2099-12-31.
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # Photo of the front of the administrator\\"s ID card (national emblem side). Only jpg, png, gif, and jpeg image formats are supported, and the image must not exceed 5 MB. Please provide the path of the file uploaded to OSS. The file name to be uploaded must not contain Chinese characters or special characters. For upload operations, see [Upload Files via OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # >Notice: 
        # No stamp is required for color originals of the certificate. If you upload a photocopy or black-and-white photo, you must affix the enterprise red seal to the photocopy and take a photo to upload.
        self.admin_idcard_front_face = admin_idcard_front_face
        # Administrator\\"s ID number.
        self.admin_idcard_no = admin_idcard_no
        # Photo of the back of the administrator\\"s ID card (portrait side). Only jpg, png, gif, and jpeg image formats are supported, and the image must not exceed 5 MB. Please provide the path of the file uploaded to OSS. The file name to be uploaded must not contain Chinese characters or special characters. For upload operations, see [Upload Files via OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # >Notice: 
        #  No stamp is required for color originals of the certificate. If you upload a photocopy or black-and-white photo, you must affix the enterprise red seal to the photocopy and take a photo to upload.
        self.admin_idcard_pic = admin_idcard_pic
        # Administrator ID card type. Valid values:
        # 
        # - identityCard: ID card.
        # - passport: Passport.
        # - homeReturnPermit: Mainland Travel Permit for Hong Kong and Macao Residents.
        # - TaiwanCompatriotPermit: Mainland Travel Permit for Taiwan Residents.
        # - residencePermit: Residence Permit for Hong Kong, Macao, and Taiwan Residents.
        # - other: Other.
        self.admin_idcard_type = admin_idcard_type
        # Administrator name.
        # 
        # > The administrator (also known as the operator) refers to the person who logs in to the Alibaba Cloud account and manages the SMS service. Generally, this is the operations personnel who manages qualifications, signatures, and templates and sends SMS messages under this Alibaba Cloud account, and whose phone number can receive verification codes. The administrator is not necessarily the administrator of this Alibaba Cloud account. The administrator can be the same person as the enterprise\\"s legal representative.
        self.admin_name = admin_name
        # Administrator\\"s mobile phone number. Format: +/+86/0086/86 prefix or a phone number without any prefix, for example, 1390000****.
        # 
        # This parameter is required.
        self.admin_phone_no = admin_phone_no
        # Enterprise business license information. This parameter is required when the purpose of the qualification to be modified is for use by others.
        self.business_license_pics = business_license_pics
        # Validity period of the business license. Format: YYYY-MM-DD~YYYY-MM-DD.
        # > When the certificate validity period is long-term, the end date can be set to 2099-12-31.
        self.bussiness_license_exp_date = bussiness_license_exp_date
        # Phone verification code. Please call the [RequiredPhoneCode](~~RequiredPhoneCode~~) API and pass in the **administrator\\"s phone number**, then enter the SMS verification code you receive here.
        # 
        # > You can use [ValidPhoneCode](~~ValidPhoneCode~~) to verify whether the SMS verification code is correct before passing it in.
        # 
        # This parameter is required.
        self.certify_code = certify_code
        # Enterprise name. Supported symbols are only the middle dot `·`, the Chinese symbols `【】（）`, the English symbols `()`, and the `space`. Other symbols or pure numbers are not allowed. The length must not exceed 150 characters.
        self.company_name = company_name
        # Legal person\\"s ID number.
        self.legal_person_idcard_no = legal_person_idcard_no
        # Legal person ID card type. Valid values:
        # 
        # - identityCard: ID card.
        # - passport: Passport.
        # - homeReturnPermit: Mainland Travel Permit for Hong Kong and Macao Residents.
        # - TaiwanCompatriotPermit: Mainland Travel Permit for Taiwan Residents.
        # - residencePermit: Residence Permit for Hong Kong, Macao, and Taiwan Residents.
        # - other: Other.
        self.legal_person_idcard_type = legal_person_idcard_type
        # Photo of the back of the legal representative\\"s ID card (portrait side). Only jpg, png, gif, and jpeg image formats are supported, and the image must not exceed 5 MB. Please provide the path of the file uploaded to OSS. The file name to be uploaded must not contain Chinese characters or special characters. For upload operations, see [Upload Files via OSS](https://help.aliyun.com/document_detail/2833114.html).
        # > The system will use the legal person name and ID number you provide for verification. If the verification fails, you need to upload a photo of the legal representative\\"s ID card.
        self.legal_person_id_card_back_side = legal_person_id_card_back_side
        # Validity period of the legal person ID card. Format: YYYY-MM-DD~YYYY-MM-DD.
        # > When the certificate validity period is long-term, the end date can be set to 2099-12-31.
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # Photo of the front of the legal representative\\"s ID card (national emblem side). Only jpg, png, gif, and jpeg image formats are supported, and the image must not exceed 5 MB. Please provide the path of the file uploaded to OSS. The file name to be uploaded must not contain Chinese characters or special characters. For upload operations, see [Upload Files via OSS](https://help.aliyun.com/document_detail/2833114.html).
        # > The system will use the legal person name and ID number you provide for verification. If the verification fails, you need to upload a photo of the legal representative\\"s ID card.
        self.legal_person_id_card_front_side = legal_person_id_card_front_side
        # Name of the legal representative.
        # 
        # > - If there is no legal representative information on the organization\\"s certificate, but there is information about a person in charge / chief representative or similar, please prepare the ID card photo of the corresponding person in charge or chief representative listed on the certificate.
        # > - If there is no legal representative information on the organization\\"s certificate, and there is no information about any person in charge, please prepare the name and ID card photo of the main business contact person.
        self.legal_person_name = legal_person_name
        # The review order ID. You can obtain the qualifications and their corresponding review order IDs under the current account by calling [Query Qualification List](~~QuerySmsQualificationRecord~~).
        # 
        # This parameter is required.
        self.order_id = order_id
        # Additional materials. If you have other supporting or supplementary materials, photos, etc., you can upload them here.
        self.other_files = other_files
        self.owner_id = owner_id
        # The qualification ID, that is, the ID returned when you [apply for SMS qualification](~~SubmitSmsQualification~~). You can obtain the qualification IDs under the current account by calling [Query Qualification List](~~QuerySmsQualificationRecord~~).
        # 
        # This parameter is required.
        self.qualification_group_id = qualification_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.business_license_pics:
            for v1 in self.business_license_pics:
                 if v1:
                    v1.validate()
        if self.other_files:
            for v1 in self.other_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_idcard_exp_date is not None:
            result['AdminIDCardExpDate'] = self.admin_idcard_exp_date

        if self.admin_idcard_front_face is not None:
            result['AdminIDCardFrontFace'] = self.admin_idcard_front_face

        if self.admin_idcard_no is not None:
            result['AdminIDCardNo'] = self.admin_idcard_no

        if self.admin_idcard_pic is not None:
            result['AdminIDCardPic'] = self.admin_idcard_pic

        if self.admin_idcard_type is not None:
            result['AdminIDCardType'] = self.admin_idcard_type

        if self.admin_name is not None:
            result['AdminName'] = self.admin_name

        if self.admin_phone_no is not None:
            result['AdminPhoneNo'] = self.admin_phone_no

        result['BusinessLicensePics'] = []
        if self.business_license_pics is not None:
            for k1 in self.business_license_pics:
                result['BusinessLicensePics'].append(k1.to_map() if k1 else None)

        if self.bussiness_license_exp_date is not None:
            result['BussinessLicenseExpDate'] = self.bussiness_license_exp_date

        if self.certify_code is not None:
            result['CertifyCode'] = self.certify_code

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.legal_person_idcard_no is not None:
            result['LegalPersonIDCardNo'] = self.legal_person_idcard_no

        if self.legal_person_idcard_type is not None:
            result['LegalPersonIDCardType'] = self.legal_person_idcard_type

        if self.legal_person_id_card_back_side is not None:
            result['LegalPersonIdCardBackSide'] = self.legal_person_id_card_back_side

        if self.legal_person_id_card_eff_time is not None:
            result['LegalPersonIdCardEffTime'] = self.legal_person_id_card_eff_time

        if self.legal_person_id_card_front_side is not None:
            result['LegalPersonIdCardFrontSide'] = self.legal_person_id_card_front_side

        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        result['OtherFiles'] = []
        if self.other_files is not None:
            for k1 in self.other_files:
                result['OtherFiles'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qualification_group_id is not None:
            result['QualificationGroupId'] = self.qualification_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminIDCardExpDate') is not None:
            self.admin_idcard_exp_date = m.get('AdminIDCardExpDate')

        if m.get('AdminIDCardFrontFace') is not None:
            self.admin_idcard_front_face = m.get('AdminIDCardFrontFace')

        if m.get('AdminIDCardNo') is not None:
            self.admin_idcard_no = m.get('AdminIDCardNo')

        if m.get('AdminIDCardPic') is not None:
            self.admin_idcard_pic = m.get('AdminIDCardPic')

        if m.get('AdminIDCardType') is not None:
            self.admin_idcard_type = m.get('AdminIDCardType')

        if m.get('AdminName') is not None:
            self.admin_name = m.get('AdminName')

        if m.get('AdminPhoneNo') is not None:
            self.admin_phone_no = m.get('AdminPhoneNo')

        self.business_license_pics = []
        if m.get('BusinessLicensePics') is not None:
            for k1 in m.get('BusinessLicensePics'):
                temp_model = main_models.UpdateSmsQualificationRequestBusinessLicensePics()
                self.business_license_pics.append(temp_model.from_map(k1))

        if m.get('BussinessLicenseExpDate') is not None:
            self.bussiness_license_exp_date = m.get('BussinessLicenseExpDate')

        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('LegalPersonIDCardNo') is not None:
            self.legal_person_idcard_no = m.get('LegalPersonIDCardNo')

        if m.get('LegalPersonIDCardType') is not None:
            self.legal_person_idcard_type = m.get('LegalPersonIDCardType')

        if m.get('LegalPersonIdCardBackSide') is not None:
            self.legal_person_id_card_back_side = m.get('LegalPersonIdCardBackSide')

        if m.get('LegalPersonIdCardEffTime') is not None:
            self.legal_person_id_card_eff_time = m.get('LegalPersonIdCardEffTime')

        if m.get('LegalPersonIdCardFrontSide') is not None:
            self.legal_person_id_card_front_side = m.get('LegalPersonIdCardFrontSide')

        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        self.other_files = []
        if m.get('OtherFiles') is not None:
            for k1 in m.get('OtherFiles'):
                temp_model = main_models.UpdateSmsQualificationRequestOtherFiles()
                self.other_files.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QualificationGroupId') is not None:
            self.qualification_group_id = m.get('QualificationGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class UpdateSmsQualificationRequestOtherFiles(DaraModel):
    def __init__(
        self,
        license_pic: str = None,
    ):
        # Additional material file. Only png, jpg, jpeg, doc, docx, and pdf formats are supported, and the file must not exceed 5 MB. Please provide the path of the file uploaded to OSS. The file name to be uploaded must not contain Chinese characters or special characters. For upload operations, see [Upload Files via OSS](https://help.aliyun.com/document_detail/2833114.html).
        self.license_pic = license_pic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')

        return self

class UpdateSmsQualificationRequestBusinessLicensePics(DaraModel):
    def __init__(
        self,
        license_pic: str = None,
        type: str = None,
    ):
        # Business license image. Only jpg, png, gif, and jpeg image formats are supported, and the image must not exceed 5 MB. Please provide the path of the file uploaded to OSS. The file name to be uploaded must not contain Chinese characters or special characters. For upload operations, see [Upload Files via OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # >Notice: 
        # No stamp is required for color originals of the certificate. If you upload a photocopy or black-and-white photo, you must affix the enterprise red seal to the photocopy and take a photo to upload.
        self.license_pic = license_pic
        # Business license type. Valid values:
        # 
        # - socialCreditLicense: Social credit code certificate.
        # - businessLicense: Enterprise business license.
        # - signLegalLicense: Public institution legal person certificate.
        # - otherLicense: Other.
        # 
        # Choose one to upload. The certificate must contain: enterprise name, unified social credit code, and certificate validity period.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

