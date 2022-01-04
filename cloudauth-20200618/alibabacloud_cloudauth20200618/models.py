# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, List


class ContrastSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        face_pic_file: str = None,
        face_pic_string: str = None,
        face_pic_url: str = None,
        ip: str = None,
        mobile: str = None,
        mode: str = None,
        outer_order_no: str = None,
        scene_id: int = None,
        user_id: str = None,
    ):
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.face_pic_file = face_pic_file
        self.face_pic_string = face_pic_string
        self.face_pic_url = face_pic_url
        self.ip = ip
        self.mobile = mobile
        self.mode = mode
        self.outer_order_no = outer_order_no
        self.scene_id = scene_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.face_pic_file is not None:
            result['FacePicFile'] = self.face_pic_file
        if self.face_pic_string is not None:
            result['FacePicString'] = self.face_pic_string
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('FacePicFile') is not None:
            self.face_pic_file = m.get('FacePicFile')
        if m.get('FacePicString') is not None:
            self.face_pic_string = m.get('FacePicString')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ContrastSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        passed: str = None,
        risk_info: str = None,
        sub_code: str = None,
        verify_info: str = None,
    ):
        self.certify_id = certify_id
        self.passed = passed
        self.risk_info = risk_info
        self.sub_code = sub_code
        self.verify_info = verify_info

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.risk_info, 'risk_info')
        self.validate_required(self.sub_code, 'sub_code')
        self.validate_required(self.verify_info, 'verify_info')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.verify_info is not None:
            result['VerifyInfo'] = self.verify_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('RiskInfo') is not None:
            self.risk_info = m.get('RiskInfo')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('VerifyInfo') is not None:
            self.verify_info = m.get('VerifyInfo')
        return self


class ContrastSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: ContrastSmartVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = ContrastSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class ContrastSmartVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        face_pic_file_object: BinaryIO = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        face_pic_string: str = None,
        face_pic_url: str = None,
        ip: str = None,
        mobile: str = None,
        mode: str = None,
        outer_order_no: str = None,
        scene_id: int = None,
        user_id: str = None,
    ):
        self.face_pic_file_object = face_pic_file_object
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.face_pic_string = face_pic_string
        self.face_pic_url = face_pic_url
        self.ip = ip
        self.mobile = mobile
        self.mode = mode
        self.outer_order_no = outer_order_no
        self.scene_id = scene_id
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.face_pic_file_object, 'face_pic_file_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_pic_file_object is not None:
            result['FacePicFileObject'] = self.face_pic_file_object
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.face_pic_string is not None:
            result['FacePicString'] = self.face_pic_string
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FacePicFileObject') is not None:
            self.face_pic_file_object = m.get('FacePicFileObject')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('FacePicString') is not None:
            self.face_pic_string = m.get('FacePicString')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        picture_return_type: str = None,
        scene_id: int = None,
    ):
        self.certify_id = certify_id
        self.picture_return_type = picture_return_type
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.picture_return_type is not None:
            result['PictureReturnType'] = self.picture_return_type
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('PictureReturnType') is not None:
            self.picture_return_type = m.get('PictureReturnType')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DescribeSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        material_info: str = None,
        passed: str = None,
        passed_score: float = None,
        sub_code: str = None,
    ):
        self.material_info = material_info
        self.passed = passed
        self.passed_score = passed_score
        self.sub_code = sub_code

    def validate(self):
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.passed_score, 'passed_score')
        self.validate_required(self.sub_code, 'sub_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.passed_score is not None:
            result['PassedScore'] = self.passed_score
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('PassedScore') is not None:
            self.passed_score = m.get('PassedScore')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class DescribeSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: DescribeSmartVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = DescribeSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class DescribeSmsDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        current_page: int = None,
        error_code: str = None,
        mobile: str = None,
        outer_order_no: str = None,
        page_size: int = None,
        send_date: str = None,
        send_status: str = None,
        sign_name: str = None,
        template_code: str = None,
    ):
        self.biz_id = biz_id
        self.current_page = current_page
        self.error_code = error_code
        self.mobile = mobile
        self.outer_order_no = outer_order_no
        self.page_size = page_size
        self.send_date = send_date
        self.send_status = send_status
        self.sign_name = sign_name
        self.template_code = template_code

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.send_date, 'send_date')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DescribeSmsDetailResponseItems(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        content: str = None,
        error_code: str = None,
        error_message: str = None,
        mobile: str = None,
        outer_order_no: str = None,
        receive_date: str = None,
        send_date: str = None,
        send_status: str = None,
        sign_name: str = None,
        sms_size: int = None,
        task_date: str = None,
        template_code: str = None,
    ):
        self.biz_id = biz_id
        self.content = content
        self.error_code = error_code
        self.error_message = error_message
        self.mobile = mobile
        self.outer_order_no = outer_order_no
        self.receive_date = receive_date
        self.send_date = send_date
        self.send_status = send_status
        self.sign_name = sign_name
        self.sms_size = sms_size
        self.task_date = task_date
        self.template_code = template_code

    def validate(self):
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.content, 'content')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.mobile, 'mobile')
        self.validate_required(self.outer_order_no, 'outer_order_no')
        self.validate_required(self.receive_date, 'receive_date')
        self.validate_required(self.send_date, 'send_date')
        self.validate_required(self.send_status, 'send_status')
        self.validate_required(self.sign_name, 'sign_name')
        self.validate_required(self.sms_size, 'sms_size')
        self.validate_required(self.task_date, 'task_date')
        self.validate_required(self.template_code, 'template_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.content is not None:
            result['Content'] = self.content
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.receive_date is not None:
            result['ReceiveDate'] = self.receive_date
        if self.send_date is not None:
            result['SendDate'] = self.send_date
        if self.send_status is not None:
            result['SendStatus'] = self.send_status
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.sms_size is not None:
            result['SmsSize'] = self.sms_size
        if self.task_date is not None:
            result['TaskDate'] = self.task_date
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('ReceiveDate') is not None:
            self.receive_date = m.get('ReceiveDate')
        if m.get('SendDate') is not None:
            self.send_date = m.get('SendDate')
        if m.get('SendStatus') is not None:
            self.send_status = m.get('SendStatus')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('SmsSize') is not None:
            self.sms_size = m.get('SmsSize')
        if m.get('TaskDate') is not None:
            self.task_date = m.get('TaskDate')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        return self


class DescribeSmsDetailResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        total_item: int = None,
        total_page: int = None,
        items: List[DescribeSmsDetailResponseItems] = None,
    ):
        self.code = code
        self.current_page = current_page
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.total_item = total_item
        self.total_page = total_page
        self.items = items

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.message, 'message')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_item, 'total_item')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_item is not None:
            result['TotalItem'] = self.total_item
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalItem') is not None:
            self.total_item = m.get('TotalItem')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSmsDetailResponseItems()
                self.items.append(temp_model.from_map(k))
        return self


class ElementSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        cert_file: str = None,
        cert_name: str = None,
        cert_national_emblem_url: str = None,
        cert_no: str = None,
        cert_type: str = None,
        cert_url: str = None,
        mode: str = None,
        outer_order_no: str = None,
        scene_id: int = None,
    ):
        self.cert_file = cert_file
        self.cert_name = cert_name
        self.cert_national_emblem_url = cert_national_emblem_url
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.cert_url = cert_url
        self.mode = mode
        self.outer_order_no = outer_order_no
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_file is not None:
            result['CertFile'] = self.cert_file
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_national_emblem_url is not None:
            result['CertNationalEmblemUrl'] = self.cert_national_emblem_url
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFile') is not None:
            self.cert_file = m.get('CertFile')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNationalEmblemUrl') is not None:
            self.cert_national_emblem_url = m.get('CertNationalEmblemUrl')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ElementSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        material_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        self.certify_id = certify_id
        self.material_info = material_info
        self.passed = passed
        self.sub_code = sub_code

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.sub_code, 'sub_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class ElementSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: ElementSmartVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = ElementSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class ElementSmartVerifyAdvanceRequest(TeaModel):
    def __init__(
        self,
        cert_file_object: BinaryIO = None,
        cert_name: str = None,
        cert_national_emblem_url: str = None,
        cert_no: str = None,
        cert_type: str = None,
        cert_url: str = None,
        mode: str = None,
        outer_order_no: str = None,
        scene_id: int = None,
    ):
        self.cert_file_object = cert_file_object
        self.cert_name = cert_name
        self.cert_national_emblem_url = cert_national_emblem_url
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.cert_url = cert_url
        self.mode = mode
        self.outer_order_no = outer_order_no
        self.scene_id = scene_id

    def validate(self):
        self.validate_required(self.cert_file_object, 'cert_file_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_file_object is not None:
            result['CertFileObject'] = self.cert_file_object
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_national_emblem_url is not None:
            result['CertNationalEmblemUrl'] = self.cert_national_emblem_url
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_url is not None:
            result['CertUrl'] = self.cert_url
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertFileObject') is not None:
            self.cert_file_object = m.get('CertFileObject')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNationalEmblemUrl') is not None:
            self.cert_national_emblem_url = m.get('CertNationalEmblemUrl')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertUrl') is not None:
            self.cert_url = m.get('CertUrl')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class InitSmartVerifyRequest(TeaModel):
    def __init__(
        self,
        callback_token: str = None,
        callback_url: str = None,
        cert_name: str = None,
        cert_no: str = None,
        cert_type: str = None,
        certify_id: str = None,
        face_picture_base_64: str = None,
        face_picture_url: str = None,
        id_name: str = None,
        id_no: str = None,
        ip: str = None,
        meta_info: str = None,
        mobile: str = None,
        mode: str = None,
        ocr: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        outer_order_no: str = None,
        scene_id: int = None,
        user_id: str = None,
    ):
        self.callback_token = callback_token
        self.callback_url = callback_url
        self.cert_name = cert_name
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.certify_id = certify_id
        self.face_picture_base_64 = face_picture_base_64
        self.face_picture_url = face_picture_url
        self.id_name = id_name
        self.id_no = id_no
        self.ip = ip
        self.meta_info = meta_info
        self.mobile = mobile
        self.mode = mode
        self.ocr = ocr
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        self.outer_order_no = outer_order_no
        self.scene_id = scene_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_token is not None:
            result['CallbackToken'] = self.callback_token
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_no is not None:
            result['CertNo'] = self.cert_no
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.face_picture_base_64 is not None:
            result['FacePictureBase64'] = self.face_picture_base_64
        if self.face_picture_url is not None:
            result['FacePictureUrl'] = self.face_picture_url
        if self.id_name is not None:
            result['IdName'] = self.id_name
        if self.id_no is not None:
            result['IdNo'] = self.id_no
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ocr is not None:
            result['Ocr'] = self.ocr
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackToken') is not None:
            self.callback_token = m.get('CallbackToken')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertNo') is not None:
            self.cert_no = m.get('CertNo')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('FacePictureBase64') is not None:
            self.face_picture_base_64 = m.get('FacePictureBase64')
        if m.get('FacePictureUrl') is not None:
            self.face_picture_url = m.get('FacePictureUrl')
        if m.get('IdName') is not None:
            self.id_name = m.get('IdName')
        if m.get('IdNo') is not None:
            self.id_no = m.get('IdNo')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Ocr') is not None:
            self.ocr = m.get('Ocr')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class InitSmartVerifyResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        self.certify_id = certify_id

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        return self


class InitSmartVerifyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: InitSmartVerifyResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = InitSmartVerifyResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class SendSmsRequest(TeaModel):
    def __init__(
        self,
        mobile: str = None,
        outer_order_no: str = None,
        sign_name: str = None,
        template_code: str = None,
        template_param: str = None,
    ):
        self.mobile = mobile
        self.outer_order_no = outer_order_no
        self.sign_name = sign_name
        self.template_code = template_code
        self.template_param = template_param

    def validate(self):
        self.validate_required(self.mobile, 'mobile')
        self.validate_required(self.sign_name, 'sign_name')
        self.validate_required(self.template_code, 'template_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        return self


class SendSmsResponseResultObject(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        self.validate_required(self.biz_id, 'biz_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class SendSmsResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: SendSmsResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = SendSmsResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VerifyBankElementRequest(TeaModel):
    def __init__(
        self,
        bank_card_file: str = None,
        bank_card_no: str = None,
        bank_card_url: str = None,
        id_name: str = None,
        id_no: str = None,
        mobile: str = None,
        mode: str = None,
        outer_order_no: str = None,
        scene_id: int = None,
    ):
        self.bank_card_file = bank_card_file
        self.bank_card_no = bank_card_no
        self.bank_card_url = bank_card_url
        self.id_name = id_name
        self.id_no = id_no
        self.mobile = mobile
        self.mode = mode
        self.outer_order_no = outer_order_no
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bank_card_file is not None:
            result['BankCardFile'] = self.bank_card_file
        if self.bank_card_no is not None:
            result['BankCardNo'] = self.bank_card_no
        if self.bank_card_url is not None:
            result['BankCardUrl'] = self.bank_card_url
        if self.id_name is not None:
            result['IdName'] = self.id_name
        if self.id_no is not None:
            result['IdNo'] = self.id_no
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BankCardFile') is not None:
            self.bank_card_file = m.get('BankCardFile')
        if m.get('BankCardNo') is not None:
            self.bank_card_no = m.get('BankCardNo')
        if m.get('BankCardUrl') is not None:
            self.bank_card_url = m.get('BankCardUrl')
        if m.get('IdName') is not None:
            self.id_name = m.get('IdName')
        if m.get('IdNo') is not None:
            self.id_no = m.get('IdNo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class VerifyBankElementResponseResultObject(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
        material_info: str = None,
        passed: str = None,
        sub_code: str = None,
    ):
        self.certify_id = certify_id
        self.material_info = material_info
        self.passed = passed
        self.sub_code = sub_code

    def validate(self):
        self.validate_required(self.certify_id, 'certify_id')
        self.validate_required(self.material_info, 'material_info')
        self.validate_required(self.passed, 'passed')
        self.validate_required(self.sub_code, 'sub_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        return self


class VerifyBankElementResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: VerifyBankElementResponseResultObject = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result_object = result_object

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultObject') is not None:
            temp_model = VerifyBankElementResponseResultObject()
            self.result_object = temp_model.from_map(m['ResultObject'])
        return self


class VerifyBankElementAdvanceRequest(TeaModel):
    def __init__(
        self,
        bank_card_file_object: BinaryIO = None,
        bank_card_no: str = None,
        bank_card_url: str = None,
        id_name: str = None,
        id_no: str = None,
        mobile: str = None,
        mode: str = None,
        outer_order_no: str = None,
        scene_id: int = None,
    ):
        self.bank_card_file_object = bank_card_file_object
        self.bank_card_no = bank_card_no
        self.bank_card_url = bank_card_url
        self.id_name = id_name
        self.id_no = id_no
        self.mobile = mobile
        self.mode = mode
        self.outer_order_no = outer_order_no
        self.scene_id = scene_id

    def validate(self):
        self.validate_required(self.bank_card_file_object, 'bank_card_file_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bank_card_file_object is not None:
            result['BankCardFileObject'] = self.bank_card_file_object
        if self.bank_card_no is not None:
            result['BankCardNo'] = self.bank_card_no
        if self.bank_card_url is not None:
            result['BankCardUrl'] = self.bank_card_url
        if self.id_name is not None:
            result['IdName'] = self.id_name
        if self.id_no is not None:
            result['IdNo'] = self.id_no
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outer_order_no is not None:
            result['OuterOrderNo'] = self.outer_order_no
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BankCardFileObject') is not None:
            self.bank_card_file_object = m.get('BankCardFileObject')
        if m.get('BankCardNo') is not None:
            self.bank_card_no = m.get('BankCardNo')
        if m.get('BankCardUrl') is not None:
            self.bank_card_url = m.get('BankCardUrl')
        if m.get('IdName') is not None:
            self.id_name = m.get('IdName')
        if m.get('IdNo') is not None:
            self.id_no = m.get('IdNo')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OuterOrderNo') is not None:
            self.outer_order_no = m.get('OuterOrderNo')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


