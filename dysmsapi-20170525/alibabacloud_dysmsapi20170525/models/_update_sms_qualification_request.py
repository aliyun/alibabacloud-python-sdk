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
        # 经办人身份证有效期，格式示例2023-01-01~2033-01-01
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # 经办人身份证照片国徽面
        self.admin_idcard_front_face = admin_idcard_front_face
        # 经办人身份证号码
        self.admin_idcard_no = admin_idcard_no
        # 经办人身份证照片人像面
        self.admin_idcard_pic = admin_idcard_pic
        # 管理员身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        self.admin_idcard_type = admin_idcard_type
        # 经办人姓名
        self.admin_name = admin_name
        # 经办人手机号码
        # 
        # This parameter is required.
        self.admin_phone_no = admin_phone_no
        # 企业证件信息
        self.business_license_pics = business_license_pics
        # 企业营业时间开始和结束字符串，格式示例2023-01-01~2033-01-01
        self.bussiness_license_exp_date = bussiness_license_exp_date
        # 手机号验证码
        # 
        # This parameter is required.
        self.certify_code = certify_code
        # 公司名称
        self.company_name = company_name
        # 法人身份证号码
        self.legal_person_idcard_no = legal_person_idcard_no
        # 法人身份证类型。identityCard:中国居民身份证;passport:护照;homeReturnPermit:港澳居民来往内地通行证;TaiwanCompatriotPermit:台湾居民来往大陆通行证;residencePermit:港澳台居民居住证";other:其他
        self.legal_person_idcard_type = legal_person_idcard_type
        # 法人身份证照片人像面
        self.legal_person_id_card_back_side = legal_person_id_card_back_side
        # 法人身份证有效期，格式示例2023-01-01~2033-01-01
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # 法人身份照片证国徽面
        self.legal_person_id_card_front_side = legal_person_id_card_front_side
        # 法人姓名
        self.legal_person_name = legal_person_name
        # 工单ID
        # 
        # This parameter is required.
        self.order_id = order_id
        # 更多资料
        self.other_files = other_files
        self.owner_id = owner_id
        # 资质组ID
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
        # 证件图片标识的osskey
        self.license_pic = license_pic
        # 企业证件类型，businessLicense:营业执照;organizationCodeLicense:组织机构代码证;taxRegistrationLicense:税务登记证;socialCreditLicense:社会信用代码证书;newStyleBusinessLicense:三证合一;signLegalLicense:签名归属方的事业单位法人证书;otherLicense:其他类型执照证书
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

