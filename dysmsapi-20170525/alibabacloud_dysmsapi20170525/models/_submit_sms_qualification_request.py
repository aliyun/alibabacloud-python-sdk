# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class SubmitSmsQualificationRequest(DaraModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics: List[main_models.SubmitSmsQualificationRequestBusinessLicensePics] = None,
        bussiness_license_exp_date: str = None,
        certify_code: str = None,
        company_name: str = None,
        company_type: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_back_side: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_id_card_front_side: str = None,
        legal_person_name: str = None,
        organization_code: str = None,
        other_files: List[main_models.SubmitSmsQualificationRequestOtherFiles] = None,
        owner_id: int = None,
        qualification_name: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        use_by_self: bool = None,
        whether_share: bool = None,
    ):
        # The administrator\\"s ID card validity period. Format: YYYY-MM-DD~YYYY-MM-DD.
        # > If the ID card has a long-term validity period, set the end date to 2099-12-31.
        # 
        # This parameter is required.
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # The front photo of the administrator\\"s ID card (national emblem side). Only jpg, png, gif, and jpeg formats are supported. The image must not exceed 5 MB. Specify the file path uploaded to OSS. The file name must not contain Chinese characters or special characters. For upload instructions, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # >Notice: 
        # Color originals do not require a stamp. If you upload a photocopy or black-and-white photo, stamp the photocopy with the company seal and take a photo to upload.
        # 
        # .
        # 
        # This parameter is required.
        self.admin_idcard_front_face = admin_idcard_front_face
        # The administrator\\"s ID card number.
        # 
        # This parameter is required.
        self.admin_idcard_no = admin_idcard_no
        # The back photo of the administrator\\"s ID card (portrait side). Only jpg, png, gif, and jpeg formats are supported. The image must not exceed 5 MB. Specify the file path uploaded to OSS. The file name must not contain Chinese characters or special characters. For upload instructions, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # >Notice: 
        # Color originals do not require a stamp. If you upload a photocopy or black-and-white photo, stamp the photocopy with the company seal and take a photo to upload.
        # 
        # .
        # 
        # This parameter is required.
        self.admin_idcard_pic = admin_idcard_pic
        # The administrator\\"s ID card type. Valid values:
        # 
        # - identityCard: ID card.
        # - passport: passport.
        # - homeReturnPermit: Hong Kong/Macao resident travel permit to mainland.
        # - TaiwanCompatriotPermit: Taiwan resident travel permit to mainland.
        # - residencePermit: Hong Kong/Macao/Taiwan resident residence permit.
        # - other: other.
        # 
        # This parameter is required.
        self.admin_idcard_type = admin_idcard_type
        # The administrator\\"s name. Maximum length: 50 characters. **Under the current [SMS signature real-name requirements](https://help.aliyun.com/document_detail/2873145.html), if the same administrator applies for qualifications for multiple different enterprises, carrier registration will fail. Ensure one administrator per enterprise to improve the registration success rate.**
        # 
        # > The administrator (also called the handler) is the person who logs on to the Alibaba Cloud account and manages SMS services. This person typically manages qualifications, signatures, and templates under this Alibaba Cloud account and performs SMS sending operations. This person\\"s phone number must be able to receive verification codes. The administrator does not have to be the Alibaba Cloud account administrator and can be the same person as the legal representative.
        # 
        # This parameter is required.
        self.admin_name = admin_name
        # The administrator\\"s phone number. Format: +/+86/0086/86 or a phone number without any prefix, such as 1390000****.
        # 
        # This parameter is required.
        self.admin_phone_no = admin_phone_no
        # The business license information. This parameter is required when the qualification purpose `UseBySelf` is set to `false` (third-party use).
        # > - Based on carrier real-name registration regulatory requirements, we strongly recommend that you provide the relevant field information. Otherwise, the probability of "review rejection or carrier registration failure" increases significantly.
        self.business_license_pics = business_license_pics
        # The business license validity period. Format: YYYY-MM-DD~YYYY-MM-DD.
        # > If the certificate has a long-term validity period, set the end date to 2099-12-31.
        # 
        # This parameter is required.
        self.bussiness_license_exp_date = bussiness_license_exp_date
        # The phone verification code. Call the [RequiredPhoneCode](~~RequiredPhoneCode~~) operation with the **administrator\\"s phone number**, and then enter the SMS verification code received.
        # 
        # > You can use [ValidPhoneCode](~~ValidPhoneCode~~) to verify whether the SMS verification code is correct before passing it in.
        # 
        # This parameter is required.
        self.certify_code = certify_code
        # The enterprise name. Only the middle dot `·`, Chinese brackets `【】（）`, English parentheses `()`, and `spaces` are supported as symbols. Other symbols or pure digits are not allowed. Maximum length: 150 characters.
        # 
        # This parameter is required.
        self.company_name = company_name
        # The enterprise type. Valid values:
        # 
        # - COMPANY: enterprise.
        # 
        # - NON_PROFIT_ORGANIZATION: government agency or public institution.
        # 
        # This parameter is required.
        self.company_type = company_type
        # The legal representative\\"s ID card number.
        # 
        # This parameter is required.
        self.legal_person_idcard_no = legal_person_idcard_no
        # The legal representative\\"s ID card type. Valid values:
        # 
        # - identityCard: ID card.
        # - passport: passport.
        # - homeReturnPermit: Hong Kong/Macao resident travel permit to mainland.
        # - TaiwanCompatriotPermit: Taiwan resident travel permit to mainland.
        # - residencePermit: Hong Kong/Macao/Taiwan resident residence permit.
        # - other: other.
        # 
        # This parameter is required.
        self.legal_person_idcard_type = legal_person_idcard_type
        # The back photo of the legal representative\\"s ID card (portrait side). Only jpg, png, gif, and jpeg formats are supported. The image must not exceed 5 MB. Specify the file path uploaded to OSS. The file name must not contain Chinese characters or special characters. For upload instructions, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # > The system verifies the legal representative\\"s name and ID number you provide. If verification fails, you must upload photos of the legal representative\\"s ID card.
        self.legal_person_id_card_back_side = legal_person_id_card_back_side
        # The legal representative\\"s ID card validity period. Format: YYYY-MM-DD~YYYY-MM-DD.
        # > If the ID card has a long-term validity period, set the end date to 2099-12-31.
        # 
        # This parameter is required.
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # The front photo of the legal representative\\"s ID card (national emblem side). Only jpg, png, gif, and jpeg formats are supported. The image must not exceed 5 MB. Specify the file path uploaded to OSS. The file name must not contain Chinese characters or special characters. For upload instructions, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # 
        # > The system verifies the legal representative\\"s name and ID number you provide. If verification fails, you must upload photos of the legal representative\\"s ID card.
        self.legal_person_id_card_front_side = legal_person_id_card_front_side
        # The legal representative\\"s name. Maximum length: 50 characters.
        # 
        # > - If the organization certificate does not contain legal representative information but includes a person in charge or chief representative, prepare the ID card photos of the corresponding person in charge or chief representative listed on the certificate.
        # > - If the organization certificate contains neither legal representative information nor any person in charge, prepare the name and ID card photos of the primary business contact.
        # 
        # This parameter is required.
        self.legal_person_name = legal_person_name
        # The unified social credit code. Maximum length: 150 characters.
        # 
        # This parameter is required.
        self.organization_code = organization_code
        # Additional materials. If you have other supporting documents, notes, or photos, upload them here.
        self.other_files = other_files
        self.owner_id = owner_id
        # The qualification name, used to manage and distinguish multiple qualifications you apply for. It does not appear in SMS content. The name must be unique among your existing qualifications. Only Chinese characters, English letters, or combinations with digits are supported. Symbols or pure digits are not supported. Maximum length: 100 characters.
        # 
        # This parameter is required.
        self.qualification_name = qualification_name
        # Remarks. If you have additional information to provide or notes for the qualification verification reviewer, add a description here.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The purpose of the qualification application. Valid values:
        # 
        # - **true**: **Self-use**. The entity that owns the signature is the same as the entity verified for this account.
        # - **false**: **Third-party use**. The entity that owns the signature is different from the entity verified for this account.
        # 
        # This parameter is required.
        self.use_by_self = use_by_self
        # Qualification authorization. Specifies whether to share the qualification with other cloud communication products (such as domestic voice services and domestic number privacy protection). Sharing is available only when you apply for a **self-use qualification** and the qualification information **matches the enterprise information verified for the current Alibaba Cloud account**. Otherwise, this setting has no effect. Valid values:
        # 
        # - true: Agree. Your qualification information can be referenced during the qualification verification process of other cloud communication products, eliminating redundant verification.
        # - false: Disagree.
        # 
        # This parameter is required.
        self.whether_share = whether_share

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

        if self.company_type is not None:
            result['CompanyType'] = self.company_type

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

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        result['OtherFiles'] = []
        if self.other_files is not None:
            for k1 in self.other_files:
                result['OtherFiles'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qualification_name is not None:
            result['QualificationName'] = self.qualification_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self

        if self.whether_share is not None:
            result['WhetherShare'] = self.whether_share

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
                temp_model = main_models.SubmitSmsQualificationRequestBusinessLicensePics()
                self.business_license_pics.append(temp_model.from_map(k1))

        if m.get('BussinessLicenseExpDate') is not None:
            self.bussiness_license_exp_date = m.get('BussinessLicenseExpDate')

        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('CompanyType') is not None:
            self.company_type = m.get('CompanyType')

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

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        self.other_files = []
        if m.get('OtherFiles') is not None:
            for k1 in m.get('OtherFiles'):
                temp_model = main_models.SubmitSmsQualificationRequestOtherFiles()
                self.other_files.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QualificationName') is not None:
            self.qualification_name = m.get('QualificationName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')

        if m.get('WhetherShare') is not None:
            self.whether_share = m.get('WhetherShare')

        return self

class SubmitSmsQualificationRequestOtherFiles(DaraModel):
    def __init__(
        self,
        license_pic: str = None,
    ):
        # The additional material file. Only png, jpg, jpeg, doc, docx, and pdf formats are supported. The file must not exceed 5 MB. Specify the file path uploaded to OSS. The file name must not contain Chinese characters or special characters. For upload instructions, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
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

class SubmitSmsQualificationRequestBusinessLicensePics(DaraModel):
    def __init__(
        self,
        license_pic: str = None,
        type: str = None,
    ):
        # The business license image. Only jpg, png, gif, and jpeg formats are supported. The image must not exceed 5 MB. Specify the file path uploaded to OSS. The file name must not contain Chinese characters or special characters. For upload instructions, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # 
        # >Notice: 
        # 
        # Color originals do not require a stamp. If you upload a photocopy or black-and-white photo, stamp the photocopy with the company seal and take a photo to upload.
        # .
        self.license_pic = license_pic
        # The business license type. Valid values:
        # 
        # - socialCreditLicense: unified social credit code certificate.
        # - businessLicense: business license.
        # - signLegalLicense: public institution legal person certificate.
        # - otherLicense: other.
        # 
        # Upload one type. The certificate must contain the enterprise name, unified social credit code, and certificate validity period.
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

