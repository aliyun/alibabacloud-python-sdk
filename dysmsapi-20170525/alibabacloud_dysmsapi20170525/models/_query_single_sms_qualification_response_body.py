# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySingleSmsQualificationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QuerySingleSmsQualificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QuerySingleSmsQualificationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySingleSmsQualificationResponseBodyData(DaraModel):
    def __init__(
        self,
        admin_idcard_exp_date: str = None,
        admin_idcard_front_face: str = None,
        admin_idcard_no: str = None,
        admin_idcard_pic: str = None,
        admin_idcard_type: str = None,
        admin_name: str = None,
        admin_phone_no: str = None,
        business_license_pics: List[main_models.QuerySingleSmsQualificationResponseBodyDataBusinessLicensePics] = None,
        business_type: str = None,
        company_name: str = None,
        company_type: str = None,
        eff_time_str: str = None,
        legal_person_idcard_no: str = None,
        legal_person_idcard_type: str = None,
        legal_person_id_card_eff_time: str = None,
        legal_person_name: str = None,
        organization_code: str = None,
        other_files: List[main_models.QuerySingleSmsQualificationResponseBodyDataOtherFiles] = None,
        qualification_group_id: int = None,
        qualification_name: str = None,
        remark: str = None,
        state: str = None,
        use_by_self: bool = None,
        whether_share: bool = None,
        work_order_id: int = None,
    ):
        # 经办人身份证有效期
        self.admin_idcard_exp_date = admin_idcard_exp_date
        # 经办人身份证国徽面，产品需求，要求身份证可以分正反面上传
        self.admin_idcard_front_face = admin_idcard_front_face
        # 经办人身份证号码
        self.admin_idcard_no = admin_idcard_no
        # 经办人身份证图片地址，正反面合一
        self.admin_idcard_pic = admin_idcard_pic
        # 管理员身份证类型
        self.admin_idcard_type = admin_idcard_type
        # 经办人姓名
        self.admin_name = admin_name
        # 经办人手机号码
        self.admin_phone_no = admin_phone_no
        # 证件信息
        self.business_license_pics = business_license_pics
        # 行业类型，在当前模式下是可以用产品线code来区分
        self.business_type = business_type
        # 公司名称
        self.company_name = company_name
        # 企业类型, COMPANY:公司，政府或者事业单位:NON_PROFIT_ORGANIZATION
        self.company_type = company_type
        self.eff_time_str = eff_time_str
        # 法人身份证号码
        self.legal_person_idcard_no = legal_person_idcard_no
        # 法人身份证类型
        self.legal_person_idcard_type = legal_person_idcard_type
        # 法人身份证有效期
        self.legal_person_id_card_eff_time = legal_person_id_card_eff_time
        # 法人姓名
        self.legal_person_name = legal_person_name
        # 社会统一信用代码
        self.organization_code = organization_code
        # 更多资料
        self.other_files = other_files
        self.qualification_group_id = qualification_group_id
        # 资质名称
        self.qualification_name = qualification_name
        # 备注
        self.remark = remark
        # 当前审核状态
        self.state = state
        # 是否自用
        self.use_by_self = use_by_self
        self.whether_share = whether_share
        # 乾坤袋工单ID
        self.work_order_id = work_order_id

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

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.company_type is not None:
            result['CompanyType'] = self.company_type

        if self.eff_time_str is not None:
            result['EffTimeStr'] = self.eff_time_str

        if self.legal_person_idcard_no is not None:
            result['LegalPersonIDCardNo'] = self.legal_person_idcard_no

        if self.legal_person_idcard_type is not None:
            result['LegalPersonIDCardType'] = self.legal_person_idcard_type

        if self.legal_person_id_card_eff_time is not None:
            result['LegalPersonIdCardEffTime'] = self.legal_person_id_card_eff_time

        if self.legal_person_name is not None:
            result['LegalPersonName'] = self.legal_person_name

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        result['OtherFiles'] = []
        if self.other_files is not None:
            for k1 in self.other_files:
                result['OtherFiles'].append(k1.to_map() if k1 else None)

        if self.qualification_group_id is not None:
            result['QualificationGroupId'] = self.qualification_group_id

        if self.qualification_name is not None:
            result['QualificationName'] = self.qualification_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.state is not None:
            result['State'] = self.state

        if self.use_by_self is not None:
            result['UseBySelf'] = self.use_by_self

        if self.whether_share is not None:
            result['WhetherShare'] = self.whether_share

        if self.work_order_id is not None:
            result['WorkOrderId'] = self.work_order_id

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
                temp_model = main_models.QuerySingleSmsQualificationResponseBodyDataBusinessLicensePics()
                self.business_license_pics.append(temp_model.from_map(k1))

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('CompanyType') is not None:
            self.company_type = m.get('CompanyType')

        if m.get('EffTimeStr') is not None:
            self.eff_time_str = m.get('EffTimeStr')

        if m.get('LegalPersonIDCardNo') is not None:
            self.legal_person_idcard_no = m.get('LegalPersonIDCardNo')

        if m.get('LegalPersonIDCardType') is not None:
            self.legal_person_idcard_type = m.get('LegalPersonIDCardType')

        if m.get('LegalPersonIdCardEffTime') is not None:
            self.legal_person_id_card_eff_time = m.get('LegalPersonIdCardEffTime')

        if m.get('LegalPersonName') is not None:
            self.legal_person_name = m.get('LegalPersonName')

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        self.other_files = []
        if m.get('OtherFiles') is not None:
            for k1 in m.get('OtherFiles'):
                temp_model = main_models.QuerySingleSmsQualificationResponseBodyDataOtherFiles()
                self.other_files.append(temp_model.from_map(k1))

        if m.get('QualificationGroupId') is not None:
            self.qualification_group_id = m.get('QualificationGroupId')

        if m.get('QualificationName') is not None:
            self.qualification_name = m.get('QualificationName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UseBySelf') is not None:
            self.use_by_self = m.get('UseBySelf')

        if m.get('WhetherShare') is not None:
            self.whether_share = m.get('WhetherShare')

        if m.get('WorkOrderId') is not None:
            self.work_order_id = m.get('WorkOrderId')

        return self

class QuerySingleSmsQualificationResponseBodyDataOtherFiles(DaraModel):
    def __init__(
        self,
        license_pic: str = None,
        pic_url: str = None,
    ):
        self.license_pic = license_pic
        # 文件的完整路径
        self.pic_url = pic_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.license_pic is not None:
            result['LicensePic'] = self.license_pic

        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')

        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')

        return self

class QuerySingleSmsQualificationResponseBodyDataBusinessLicensePics(DaraModel):
    def __init__(
        self,
        license_pic: str = None,
        pic_url: str = None,
        type: str = None,
    ):
        self.license_pic = license_pic
        # 文件的完整路径
        self.pic_url = pic_url
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

        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LicensePic') is not None:
            self.license_pic = m.get('LicensePic')

        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

