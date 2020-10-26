# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class UnsubscribeDeviceEventRequest(TeaModel):
    def __init__(self, device_id=None):
        self.device_id = device_id      # type: str

    def validate(self):
        self.validate_required(self.device_id, 'device_id')

    def to_map(self):
        result = {}
        result['DeviceId'] = self.device_id
        return result

    def from_map(self, map={}):
        self.device_id = map.get('DeviceId')
        return self


class UnsubscribeDeviceEventResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class ListSubscribeDeviceRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class ListSubscribeDeviceResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListSubscribeDeviceResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListSubscribeDeviceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListSubscribeDeviceResponseDataSubscribeList(TeaModel):
    def __init__(self, user_id=None, device_id=None, push_config=None, create_time=None, update_time=None):
        self.user_id = user_id          # type: str
        self.device_id = device_id      # type: str
        self.push_config = push_config  # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.push_config, 'push_config')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')

    def to_map(self):
        result = {}
        result['UserId'] = self.user_id
        result['DeviceId'] = self.device_id
        result['PushConfig'] = self.push_config
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        return result

    def from_map(self, map={}):
        self.user_id = map.get('UserId')
        self.device_id = map.get('DeviceId')
        self.push_config = map.get('PushConfig')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        return self


class ListSubscribeDeviceResponseData(TeaModel):
    def __init__(self, total_count=None, subscribe_list=None):
        self.total_count = total_count  # type: int
        self.subscribe_list = subscribe_list  # type: List[ListSubscribeDeviceResponseDataSubscribeList]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.subscribe_list, 'subscribe_list')
        if self.subscribe_list:
            for k in self.subscribe_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['SubscribeList'] = []
        if self.subscribe_list is not None:
            for k in self.subscribe_list:
                result['SubscribeList'].append(k.to_map() if k else None)
        else:
            result['SubscribeList'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.subscribe_list = []
        if map.get('SubscribeList') is not None:
            for k in map.get('SubscribeList'):
                temp_model = ListSubscribeDeviceResponseDataSubscribeList()
                self.subscribe_list.append(temp_model.from_map(k))
        else:
            self.subscribe_list = None
        return self


class SubscribeDeviceEventRequest(TeaModel):
    def __init__(self, device_id=None, push_config=None):
        self.device_id = device_id      # type: str
        self.push_config = push_config  # type: str

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.push_config, 'push_config')

    def to_map(self):
        result = {}
        result['DeviceId'] = self.device_id
        result['PushConfig'] = self.push_config
        return result

    def from_map(self, map={}):
        self.device_id = map.get('DeviceId')
        self.push_config = map.get('PushConfig')
        return self


class SubscribeDeviceEventResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class SubscribeSpaceEventRequest(TeaModel):
    def __init__(self, space_id=None, push_config=None):
        self.space_id = space_id        # type: str
        self.push_config = push_config  # type: str

    def validate(self):
        self.validate_required(self.space_id, 'space_id')
        self.validate_required(self.push_config, 'push_config')

    def to_map(self):
        result = {}
        result['SpaceId'] = self.space_id
        result['PushConfig'] = self.push_config
        return result

    def from_map(self, map={}):
        self.space_id = map.get('SpaceId')
        self.push_config = map.get('PushConfig')
        return self


class SubscribeSpaceEventResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class UnsubscribeSpaceEventRequest(TeaModel):
    def __init__(self, space_id=None):
        self.space_id = space_id        # type: str

    def validate(self):
        self.validate_required(self.space_id, 'space_id')

    def to_map(self):
        result = {}
        result['SpaceId'] = self.space_id
        return result

    def from_map(self, map={}):
        self.space_id = map.get('SpaceId')
        return self


class UnsubscribeSpaceEventResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class ListPersonTraceDetailsRequest(TeaModel):
    def __init__(self, corp_id=None, page_number=None, page_size=None, end_time=None, person_id=None,
                 start_time=None, sub_id=None, data_source_id=None):
        self.corp_id = corp_id          # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.end_time = end_time        # type: str
        self.person_id = person_id      # type: str
        self.start_time = start_time    # type: str
        self.sub_id = sub_id            # type: str
        self.data_source_id = data_source_id  # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['EndTime'] = self.end_time
        result['PersonId'] = self.person_id
        result['StartTime'] = self.start_time
        result['SubId'] = self.sub_id
        result['DataSourceId'] = self.data_source_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.end_time = map.get('EndTime')
        self.person_id = map.get('PersonId')
        self.start_time = map.get('StartTime')
        self.sub_id = map.get('SubId')
        self.data_source_id = map.get('DataSourceId')
        return self


class ListPersonTraceDetailsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, page_number=None, page_size=None, total_count=None,
                 data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.data = data                # type: List[ListPersonTraceDetailsResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListPersonTraceDetailsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListPersonTraceDetailsResponseData(TeaModel):
    def __init__(self, target_pic_url_path=None, data_source_id=None, person_id=None, pic_url_path=None,
                 right_bottom_y=None, right_bottom_x=None, shot_time=None, corp_id=None, sub_id=None, left_top_y=None,
                 left_top_x=None):
        self.target_pic_url_path = target_pic_url_path  # type: str
        self.data_source_id = data_source_id  # type: str
        self.person_id = person_id      # type: str
        self.pic_url_path = pic_url_path  # type: str
        self.right_bottom_y = right_bottom_y  # type: str
        self.right_bottom_x = right_bottom_x  # type: str
        self.shot_time = shot_time      # type: str
        self.corp_id = corp_id          # type: str
        self.sub_id = sub_id            # type: str
        self.left_top_y = left_top_y    # type: str
        self.left_top_x = left_top_x    # type: str

    def validate(self):
        self.validate_required(self.target_pic_url_path, 'target_pic_url_path')
        self.validate_required(self.data_source_id, 'data_source_id')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.pic_url_path, 'pic_url_path')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.sub_id, 'sub_id')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.left_top_x, 'left_top_x')

    def to_map(self):
        result = {}
        result['TargetPicUrlPath'] = self.target_pic_url_path
        result['DataSourceId'] = self.data_source_id
        result['PersonId'] = self.person_id
        result['PicUrlPath'] = self.pic_url_path
        result['RightBottomY'] = self.right_bottom_y
        result['RightBottomX'] = self.right_bottom_x
        result['ShotTime'] = self.shot_time
        result['CorpId'] = self.corp_id
        result['SubId'] = self.sub_id
        result['LeftTopY'] = self.left_top_y
        result['LeftTopX'] = self.left_top_x
        return result

    def from_map(self, map={}):
        self.target_pic_url_path = map.get('TargetPicUrlPath')
        self.data_source_id = map.get('DataSourceId')
        self.person_id = map.get('PersonId')
        self.pic_url_path = map.get('PicUrlPath')
        self.right_bottom_y = map.get('RightBottomY')
        self.right_bottom_x = map.get('RightBottomX')
        self.shot_time = map.get('ShotTime')
        self.corp_id = map.get('CorpId')
        self.sub_id = map.get('SubId')
        self.left_top_y = map.get('LeftTopY')
        self.left_top_x = map.get('LeftTopX')
        return self


class GetMonitorListRequest(TeaModel):
    def __init__(self, corp_id=None, page_no=None, page_size=None):
        self.corp_id = corp_id          # type: str
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        return self


class GetMonitorListResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetMonitorListResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetMonitorListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMonitorListResponseDataRecords(TeaModel):
    def __init__(self, task_id=None, status=None, monitor_type=None, rule_name=None, algorithm_vendor=None,
                 create_date=None, modified_date=None, device_list=None, attributes=None, rule_expression=None,
                 notifier_type=None, notifier_extra=None, description=None, expression=None, image_match=None):
        self.task_id = task_id          # type: str
        self.status = status            # type: str
        self.monitor_type = monitor_type  # type: str
        self.rule_name = rule_name      # type: str
        self.algorithm_vendor = algorithm_vendor  # type: str
        self.create_date = create_date  # type: str
        self.modified_date = modified_date  # type: str
        self.device_list = device_list  # type: str
        self.attributes = attributes    # type: str
        self.rule_expression = rule_expression  # type: str
        self.notifier_type = notifier_type  # type: str
        self.notifier_extra = notifier_extra  # type: str
        self.description = description  # type: str
        self.expression = expression    # type: str
        self.image_match = image_match  # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.monitor_type, 'monitor_type')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.algorithm_vendor, 'algorithm_vendor')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.modified_date, 'modified_date')
        self.validate_required(self.device_list, 'device_list')
        self.validate_required(self.attributes, 'attributes')
        self.validate_required(self.rule_expression, 'rule_expression')
        self.validate_required(self.notifier_type, 'notifier_type')
        self.validate_required(self.notifier_extra, 'notifier_extra')
        self.validate_required(self.description, 'description')
        self.validate_required(self.expression, 'expression')
        self.validate_required(self.image_match, 'image_match')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['Status'] = self.status
        result['MonitorType'] = self.monitor_type
        result['RuleName'] = self.rule_name
        result['AlgorithmVendor'] = self.algorithm_vendor
        result['CreateDate'] = self.create_date
        result['ModifiedDate'] = self.modified_date
        result['DeviceList'] = self.device_list
        result['Attributes'] = self.attributes
        result['RuleExpression'] = self.rule_expression
        result['NotifierType'] = self.notifier_type
        result['NotifierExtra'] = self.notifier_extra
        result['Description'] = self.description
        result['Expression'] = self.expression
        result['ImageMatch'] = self.image_match
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.status = map.get('Status')
        self.monitor_type = map.get('MonitorType')
        self.rule_name = map.get('RuleName')
        self.algorithm_vendor = map.get('AlgorithmVendor')
        self.create_date = map.get('CreateDate')
        self.modified_date = map.get('ModifiedDate')
        self.device_list = map.get('DeviceList')
        self.attributes = map.get('Attributes')
        self.rule_expression = map.get('RuleExpression')
        self.notifier_type = map.get('NotifierType')
        self.notifier_extra = map.get('NotifierExtra')
        self.description = map.get('Description')
        self.expression = map.get('Expression')
        self.image_match = map.get('ImageMatch')
        return self


class GetMonitorListResponseData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[GetMonitorListResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = GetMonitorListResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class ListDeviceGroupsRequest(TeaModel):
    def __init__(self, device_code_list=None, corp_id_list=None, name=None, is_page=None, page_num=None,
                 page_size=None, group=None):
        self.device_code_list = device_code_list  # type: str
        self.corp_id_list = corp_id_list  # type: str
        self.name = name                # type: str
        self.is_page = is_page          # type: int
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.group = group              # type: str

    def validate(self):
        self.validate_required(self.is_page, 'is_page')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['DeviceCodeList'] = self.device_code_list
        result['CorpIdList'] = self.corp_id_list
        result['Name'] = self.name
        result['IsPage'] = self.is_page
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Group'] = self.group
        return result

    def from_map(self, map={}):
        self.device_code_list = map.get('DeviceCodeList')
        self.corp_id_list = map.get('CorpIdList')
        self.name = map.get('Name')
        self.is_page = map.get('IsPage')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.group = map.get('Group')
        return self


class ListDeviceGroupsResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: List[ListDeviceGroupsResponseData]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListDeviceGroupsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListDeviceGroupsResponseDataList(TeaModel):
    def __init__(self, device_group=None, device_name=None, device_code=None, bit_rate=None, coding_format=None,
                 resolving_power=None, data_source_type=None, region_name=None, region_id=None, install_address=None,
                 device_sn=None, device_status=None, device_stream_status=None, device_compute_status=None):
        self.device_group = device_group  # type: str
        self.device_name = device_name  # type: str
        self.device_code = device_code  # type: str
        self.bit_rate = bit_rate        # type: str
        self.coding_format = coding_format  # type: str
        self.resolving_power = resolving_power  # type: str
        self.data_source_type = data_source_type  # type: str
        self.region_name = region_name  # type: str
        self.region_id = region_id      # type: str
        self.install_address = install_address  # type: str
        self.device_sn = device_sn      # type: str
        self.device_status = device_status  # type: str
        self.device_stream_status = device_stream_status  # type: str
        self.device_compute_status = device_compute_status  # type: str

    def validate(self):
        self.validate_required(self.device_group, 'device_group')
        self.validate_required(self.device_name, 'device_name')
        self.validate_required(self.device_code, 'device_code')
        self.validate_required(self.bit_rate, 'bit_rate')
        self.validate_required(self.coding_format, 'coding_format')
        self.validate_required(self.resolving_power, 'resolving_power')
        self.validate_required(self.data_source_type, 'data_source_type')
        self.validate_required(self.region_name, 'region_name')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.install_address, 'install_address')
        self.validate_required(self.device_sn, 'device_sn')
        self.validate_required(self.device_status, 'device_status')
        self.validate_required(self.device_stream_status, 'device_stream_status')
        self.validate_required(self.device_compute_status, 'device_compute_status')

    def to_map(self):
        result = {}
        result['DeviceGroup'] = self.device_group
        result['DeviceName'] = self.device_name
        result['DeviceCode'] = self.device_code
        result['BitRate'] = self.bit_rate
        result['CodingFormat'] = self.coding_format
        result['ResolvingPower'] = self.resolving_power
        result['DataSourceType'] = self.data_source_type
        result['RegionName'] = self.region_name
        result['RegionId'] = self.region_id
        result['InstallAddress'] = self.install_address
        result['DeviceSn'] = self.device_sn
        result['DeviceStatus'] = self.device_status
        result['DeviceStreamStatus'] = self.device_stream_status
        result['DeviceComputeStatus'] = self.device_compute_status
        return result

    def from_map(self, map={}):
        self.device_group = map.get('DeviceGroup')
        self.device_name = map.get('DeviceName')
        self.device_code = map.get('DeviceCode')
        self.bit_rate = map.get('BitRate')
        self.coding_format = map.get('CodingFormat')
        self.resolving_power = map.get('ResolvingPower')
        self.data_source_type = map.get('DataSourceType')
        self.region_name = map.get('RegionName')
        self.region_id = map.get('RegionId')
        self.install_address = map.get('InstallAddress')
        self.device_sn = map.get('DeviceSn')
        self.device_status = map.get('DeviceStatus')
        self.device_stream_status = map.get('DeviceStreamStatus')
        self.device_compute_status = map.get('DeviceComputeStatus')
        return self


class ListDeviceGroupsResponseData(TeaModel):
    def __init__(self, total_count=None, list=None):
        self.total_count = total_count  # type: str
        self.list = list                # type: List[ListDeviceGroupsResponseDataList]

    def validate(self):
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.list, 'list')
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TotalCount'] = self.total_count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        else:
            result['List'] = None
        return result

    def from_map(self, map={}):
        self.total_count = map.get('TotalCount')
        self.list = []
        if map.get('List') is not None:
            for k in map.get('List'):
                temp_model = ListDeviceGroupsResponseDataList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
        return self


class SearchObjectRequest(TeaModel):
    def __init__(self, corp_id=None, object_type=None, start_time=None, end_time=None, page_number=None,
                 page_size=None, device_list=None, pic_url=None, conditions=None, algorithm_type=None, image_path=None):
        self.corp_id = corp_id          # type: str
        self.object_type = object_type  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.device_list = device_list  # type: Dict[str, Any]
        self.pic_url = pic_url          # type: str
        self.conditions = conditions    # type: Dict[str, Any]
        self.algorithm_type = algorithm_type  # type: str
        self.image_path = image_path    # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.object_type, 'object_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['ObjectType'] = self.object_type
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['DeviceList'] = self.device_list
        result['PicUrl'] = self.pic_url
        result['Conditions'] = self.conditions
        result['AlgorithmType'] = self.algorithm_type
        result['ImagePath'] = self.image_path
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.object_type = map.get('ObjectType')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.device_list = map.get('DeviceList')
        self.pic_url = map.get('PicUrl')
        self.conditions = map.get('Conditions')
        self.algorithm_type = map.get('AlgorithmType')
        self.image_path = map.get('ImagePath')
        return self


class SearchObjectShrinkRequest(TeaModel):
    def __init__(self, corp_id=None, object_type=None, start_time=None, end_time=None, page_number=None,
                 page_size=None, device_list_shrink=None, pic_url=None, conditions_shrink=None, algorithm_type=None,
                 image_path_shrink=None):
        self.corp_id = corp_id          # type: str
        self.object_type = object_type  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.device_list_shrink = device_list_shrink  # type: str
        self.pic_url = pic_url          # type: str
        self.conditions_shrink = conditions_shrink  # type: str
        self.algorithm_type = algorithm_type  # type: str
        self.image_path_shrink = image_path_shrink  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.object_type, 'object_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['ObjectType'] = self.object_type
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['DeviceList'] = self.device_list_shrink
        result['PicUrl'] = self.pic_url
        result['Conditions'] = self.conditions_shrink
        result['AlgorithmType'] = self.algorithm_type
        result['ImagePath'] = self.image_path_shrink
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.object_type = map.get('ObjectType')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.device_list_shrink = map.get('DeviceList')
        self.pic_url = map.get('PicUrl')
        self.conditions_shrink = map.get('Conditions')
        self.algorithm_type = map.get('AlgorithmType')
        self.image_path_shrink = map.get('ImagePath')
        return self


class SearchObjectResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: SearchObjectResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SearchObjectResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class SearchObjectResponseDataRecords(TeaModel):
    def __init__(self, compare_result=None, device_id=None, shot_time=None, left_top_x=None, left_top_y=None,
                 right_btm_x=None, right_btm_y=None, score=None, source_id=None, source_image_path=None, source_image_url=None,
                 target_image_path=None, target_image_url=None):
        self.compare_result = compare_result  # type: str
        self.device_id = device_id      # type: str
        self.shot_time = shot_time      # type: int
        self.left_top_x = left_top_x    # type: int
        self.left_top_y = left_top_y    # type: int
        self.right_btm_x = right_btm_x  # type: int
        self.right_btm_y = right_btm_y  # type: int
        self.score = score              # type: float
        self.source_id = source_id      # type: str
        self.source_image_path = source_image_path  # type: str
        self.source_image_url = source_image_url  # type: str
        self.target_image_path = target_image_path  # type: str
        self.target_image_url = target_image_url  # type: str

    def validate(self):
        self.validate_required(self.compare_result, 'compare_result')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.right_btm_x, 'right_btm_x')
        self.validate_required(self.right_btm_y, 'right_btm_y')
        self.validate_required(self.score, 'score')
        self.validate_required(self.source_id, 'source_id')
        self.validate_required(self.source_image_path, 'source_image_path')
        self.validate_required(self.source_image_url, 'source_image_url')
        self.validate_required(self.target_image_path, 'target_image_path')
        self.validate_required(self.target_image_url, 'target_image_url')

    def to_map(self):
        result = {}
        result['CompareResult'] = self.compare_result
        result['DeviceID'] = self.device_id
        result['ShotTime'] = self.shot_time
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['RightBtmX'] = self.right_btm_x
        result['RightBtmY'] = self.right_btm_y
        result['Score'] = self.score
        result['SourceID'] = self.source_id
        result['SourceImagePath'] = self.source_image_path
        result['SourceImageUrl'] = self.source_image_url
        result['TargetImagePath'] = self.target_image_path
        result['TargetImageUrl'] = self.target_image_url
        return result

    def from_map(self, map={}):
        self.compare_result = map.get('CompareResult')
        self.device_id = map.get('DeviceID')
        self.shot_time = map.get('ShotTime')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.right_btm_x = map.get('RightBtmX')
        self.right_btm_y = map.get('RightBtmY')
        self.score = map.get('Score')
        self.source_id = map.get('SourceID')
        self.source_image_path = map.get('SourceImagePath')
        self.source_image_url = map.get('SourceImageUrl')
        self.target_image_path = map.get('TargetImagePath')
        self.target_image_url = map.get('TargetImageUrl')
        return self


class SearchObjectResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[SearchObjectResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = SearchObjectResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class DescribeDevicesRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, corp_id_list=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.corp_id_list = corp_id_list  # type: str

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.corp_id_list, 'corp_id_list')

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['CorpIdList'] = self.corp_id_list
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.corp_id_list = map.get('CorpIdList')
        return self


class DescribeDevicesResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: DescribeDevicesResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = DescribeDevicesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class DescribeDevicesResponseDataRecords(TeaModel):
    def __init__(self, in_protocol=None, create_time=None, device_address=None, device_id=None, device_name=None,
                 device_type=None, latitude=None, longitude=None, status=None, vendor=None, corp_id=None):
        self.in_protocol = in_protocol  # type: str
        self.create_time = create_time  # type: str
        self.device_address = device_address  # type: str
        self.device_id = device_id      # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: str
        self.latitude = latitude        # type: str
        self.longitude = longitude      # type: str
        self.status = status            # type: str
        self.vendor = vendor            # type: str
        self.corp_id = corp_id          # type: str

    def validate(self):
        self.validate_required(self.in_protocol, 'in_protocol')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.device_address, 'device_address')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.device_name, 'device_name')
        self.validate_required(self.device_type, 'device_type')
        self.validate_required(self.latitude, 'latitude')
        self.validate_required(self.longitude, 'longitude')
        self.validate_required(self.status, 'status')
        self.validate_required(self.vendor, 'vendor')
        self.validate_required(self.corp_id, 'corp_id')

    def to_map(self):
        result = {}
        result['InProtocol'] = self.in_protocol
        result['CreateTime'] = self.create_time
        result['DeviceAddress'] = self.device_address
        result['DeviceId'] = self.device_id
        result['DeviceName'] = self.device_name
        result['DeviceType'] = self.device_type
        result['Latitude'] = self.latitude
        result['Longitude'] = self.longitude
        result['Status'] = self.status
        result['Vendor'] = self.vendor
        result['CorpId'] = self.corp_id
        return result

    def from_map(self, map={}):
        self.in_protocol = map.get('InProtocol')
        self.create_time = map.get('CreateTime')
        self.device_address = map.get('DeviceAddress')
        self.device_id = map.get('DeviceId')
        self.device_name = map.get('DeviceName')
        self.device_type = map.get('DeviceType')
        self.latitude = map.get('Latitude')
        self.longitude = map.get('Longitude')
        self.status = map.get('Status')
        self.vendor = map.get('Vendor')
        self.corp_id = map.get('CorpId')
        return self


class DescribeDevicesResponseData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[DescribeDevicesResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = DescribeDevicesResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class GetProfileListRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, name=None, catalog_id=None, id_number=None, face_url=None,
                 live_address=None, gender=None, plate_no=None, phone_no=None, scene_type=None, biz_id=None, page_number=None,
                 page_size=None, person_id_list=None, profile_id_list=None, matching_rate_threshold=None, face_image_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.name = name                # type: str
        self.catalog_id = catalog_id    # type: int
        self.id_number = id_number      # type: str
        self.face_url = face_url        # type: str
        self.live_address = live_address  # type: str
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.scene_type = scene_type    # type: str
        self.biz_id = biz_id            # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.person_id_list = person_id_list  # type: Dict[str, Any]
        self.profile_id_list = profile_id_list  # type: Dict[str, Any]
        self.matching_rate_threshold = matching_rate_threshold  # type: str
        self.face_image_id = face_image_id  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['Name'] = self.name
        result['CatalogId'] = self.catalog_id
        result['IdNumber'] = self.id_number
        result['FaceUrl'] = self.face_url
        result['LiveAddress'] = self.live_address
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['SceneType'] = self.scene_type
        result['BizId'] = self.biz_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['PersonIdList'] = self.person_id_list
        result['ProfileIdList'] = self.profile_id_list
        result['MatchingRateThreshold'] = self.matching_rate_threshold
        result['FaceImageId'] = self.face_image_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.name = map.get('Name')
        self.catalog_id = map.get('CatalogId')
        self.id_number = map.get('IdNumber')
        self.face_url = map.get('FaceUrl')
        self.live_address = map.get('LiveAddress')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.scene_type = map.get('SceneType')
        self.biz_id = map.get('BizId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.person_id_list = map.get('PersonIdList')
        self.profile_id_list = map.get('ProfileIdList')
        self.matching_rate_threshold = map.get('MatchingRateThreshold')
        self.face_image_id = map.get('FaceImageId')
        return self


class GetProfileListShrinkRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, name=None, catalog_id=None, id_number=None, face_url=None,
                 live_address=None, gender=None, plate_no=None, phone_no=None, scene_type=None, biz_id=None, page_number=None,
                 page_size=None, person_id_list_shrink=None, profile_id_list_shrink=None, matching_rate_threshold=None,
                 face_image_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.name = name                # type: str
        self.catalog_id = catalog_id    # type: int
        self.id_number = id_number      # type: str
        self.face_url = face_url        # type: str
        self.live_address = live_address  # type: str
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.scene_type = scene_type    # type: str
        self.biz_id = biz_id            # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.person_id_list_shrink = person_id_list_shrink  # type: str
        self.profile_id_list_shrink = profile_id_list_shrink  # type: str
        self.matching_rate_threshold = matching_rate_threshold  # type: str
        self.face_image_id = face_image_id  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['Name'] = self.name
        result['CatalogId'] = self.catalog_id
        result['IdNumber'] = self.id_number
        result['FaceUrl'] = self.face_url
        result['LiveAddress'] = self.live_address
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['SceneType'] = self.scene_type
        result['BizId'] = self.biz_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['PersonIdList'] = self.person_id_list_shrink
        result['ProfileIdList'] = self.profile_id_list_shrink
        result['MatchingRateThreshold'] = self.matching_rate_threshold
        result['FaceImageId'] = self.face_image_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.name = map.get('Name')
        self.catalog_id = map.get('CatalogId')
        self.id_number = map.get('IdNumber')
        self.face_url = map.get('FaceUrl')
        self.live_address = map.get('LiveAddress')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.scene_type = map.get('SceneType')
        self.biz_id = map.get('BizId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.person_id_list_shrink = map.get('PersonIdList')
        self.profile_id_list_shrink = map.get('ProfileIdList')
        self.matching_rate_threshold = map.get('MatchingRateThreshold')
        self.face_image_id = map.get('FaceImageId')
        return self


class GetProfileListResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetProfileListResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetProfileListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetProfileListResponseDataRecords(TeaModel):
    def __init__(self, scene_type=None, biz_id=None, face_url=None, gender=None, id_number=None, isv_sub_id=None,
                 search_matching_rate=None, person_id=None, catalog_id=None, profile_id=None, name=None):
        self.scene_type = scene_type    # type: str
        self.biz_id = biz_id            # type: str
        self.face_url = face_url        # type: str
        self.gender = gender            # type: str
        self.id_number = id_number      # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.search_matching_rate = search_matching_rate  # type: str
        self.person_id = person_id      # type: str
        self.catalog_id = catalog_id    # type: int
        self.profile_id = profile_id    # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.scene_type, 'scene_type')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.face_url, 'face_url')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.search_matching_rate, 'search_matching_rate')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.profile_id, 'profile_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['SceneType'] = self.scene_type
        result['BizId'] = self.biz_id
        result['FaceUrl'] = self.face_url
        result['Gender'] = self.gender
        result['IdNumber'] = self.id_number
        result['IsvSubId'] = self.isv_sub_id
        result['SearchMatchingRate'] = self.search_matching_rate
        result['PersonId'] = self.person_id
        result['CatalogId'] = self.catalog_id
        result['ProfileId'] = self.profile_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.scene_type = map.get('SceneType')
        self.biz_id = map.get('BizId')
        self.face_url = map.get('FaceUrl')
        self.gender = map.get('Gender')
        self.id_number = map.get('IdNumber')
        self.isv_sub_id = map.get('IsvSubId')
        self.search_matching_rate = map.get('SearchMatchingRate')
        self.person_id = map.get('PersonId')
        self.catalog_id = map.get('CatalogId')
        self.profile_id = map.get('ProfileId')
        self.name = map.get('Name')
        return self


class GetProfileListResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, success=None, total=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.success = success          # type: bool
        self.total = total              # type: int
        self.records = records          # type: List[GetProfileListResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.success, 'success')
        self.validate_required(self.total, 'total')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Success'] = self.success
        result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.success = map.get('Success')
        self.total = map.get('Total')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = GetProfileListResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class GetProfileDetailRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, profile_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.profile_id = profile_id    # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.profile_id, 'profile_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['ProfileId'] = self.profile_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.profile_id = map.get('ProfileId')
        return self


class GetProfileDetailResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetProfileDetailResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetProfileDetailResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetProfileDetailResponseData(TeaModel):
    def __init__(self, live_address=None, scene_type=None, biz_id=None, face_url=None, gender=None, id_number=None,
                 isv_sub_id=None, phone_no=None, plate_no=None, catalog_id=None, profile_id=None, name=None, person_id=None):
        self.live_address = live_address  # type: str
        self.scene_type = scene_type    # type: str
        self.biz_id = biz_id            # type: str
        self.face_url = face_url        # type: str
        self.gender = gender            # type: str
        self.id_number = id_number      # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.phone_no = phone_no        # type: str
        self.plate_no = plate_no        # type: str
        self.catalog_id = catalog_id    # type: int
        self.profile_id = profile_id    # type: int
        self.name = name                # type: str
        self.person_id = person_id      # type: str

    def validate(self):
        self.validate_required(self.live_address, 'live_address')
        self.validate_required(self.scene_type, 'scene_type')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.face_url, 'face_url')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.phone_no, 'phone_no')
        self.validate_required(self.plate_no, 'plate_no')
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.profile_id, 'profile_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.person_id, 'person_id')

    def to_map(self):
        result = {}
        result['LiveAddress'] = self.live_address
        result['SceneType'] = self.scene_type
        result['BizId'] = self.biz_id
        result['FaceUrl'] = self.face_url
        result['Gender'] = self.gender
        result['IdNumber'] = self.id_number
        result['IsvSubId'] = self.isv_sub_id
        result['PhoneNo'] = self.phone_no
        result['PlateNo'] = self.plate_no
        result['CatalogId'] = self.catalog_id
        result['ProfileId'] = self.profile_id
        result['Name'] = self.name
        result['PersonId'] = self.person_id
        return result

    def from_map(self, map={}):
        self.live_address = map.get('LiveAddress')
        self.scene_type = map.get('SceneType')
        self.biz_id = map.get('BizId')
        self.face_url = map.get('FaceUrl')
        self.gender = map.get('Gender')
        self.id_number = map.get('IdNumber')
        self.isv_sub_id = map.get('IsvSubId')
        self.phone_no = map.get('PhoneNo')
        self.plate_no = map.get('PlateNo')
        self.catalog_id = map.get('CatalogId')
        self.profile_id = map.get('ProfileId')
        self.name = map.get('Name')
        self.person_id = map.get('PersonId')
        return self


class DeleteProfileCatalogRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, catalog_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.catalog_id = catalog_id    # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.catalog_id, 'catalog_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['CatalogId'] = self.catalog_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.catalog_id = map.get('CatalogId')
        return self


class DeleteProfileCatalogResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: bool
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class BindPersonRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, person_matching_rate=None, person_id=None, profile_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.person_matching_rate = person_matching_rate  # type: str
        self.person_id = person_id      # type: str
        self.profile_id = profile_id    # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.person_matching_rate, 'person_matching_rate')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.profile_id, 'profile_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['PersonMatchingRate'] = self.person_matching_rate
        result['PersonId'] = self.person_id
        result['ProfileId'] = self.profile_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.person_matching_rate = map.get('PersonMatchingRate')
        self.person_id = map.get('PersonId')
        self.profile_id = map.get('ProfileId')
        return self


class BindPersonResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: bool
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class UpdateProfileRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, name=None, catalog_id=None, id_number=None, face_url=None,
                 live_address=None, gender=None, plate_no=None, phone_no=None, scene_type=None, biz_id=None, profile_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.name = name                # type: str
        self.catalog_id = catalog_id    # type: int
        self.id_number = id_number      # type: str
        self.face_url = face_url        # type: str
        self.live_address = live_address  # type: str
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.scene_type = scene_type    # type: str
        self.biz_id = biz_id            # type: str
        self.profile_id = profile_id    # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.profile_id, 'profile_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['Name'] = self.name
        result['CatalogId'] = self.catalog_id
        result['IdNumber'] = self.id_number
        result['FaceUrl'] = self.face_url
        result['LiveAddress'] = self.live_address
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['SceneType'] = self.scene_type
        result['BizId'] = self.biz_id
        result['ProfileId'] = self.profile_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.name = map.get('Name')
        self.catalog_id = map.get('CatalogId')
        self.id_number = map.get('IdNumber')
        self.face_url = map.get('FaceUrl')
        self.live_address = map.get('LiveAddress')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.scene_type = map.get('SceneType')
        self.biz_id = map.get('BizId')
        self.profile_id = map.get('ProfileId')
        return self


class UpdateProfileResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class UnbindPersonRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, profile_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.profile_id = profile_id    # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.profile_id, 'profile_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['ProfileId'] = self.profile_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.profile_id = map.get('ProfileId')
        return self


class UnbindPersonResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: bool
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class AddProfileRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, name=None, catalog_id=None, id_number=None, face_url=None,
                 live_address=None, gender=None, plate_no=None, phone_no=None, scene_type=None, biz_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.name = name                # type: str
        self.catalog_id = catalog_id    # type: int
        self.id_number = id_number      # type: str
        self.face_url = face_url        # type: str
        self.live_address = live_address  # type: str
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.scene_type = scene_type    # type: str
        self.biz_id = biz_id            # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.catalog_id, 'catalog_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['Name'] = self.name
        result['CatalogId'] = self.catalog_id
        result['IdNumber'] = self.id_number
        result['FaceUrl'] = self.face_url
        result['LiveAddress'] = self.live_address
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['SceneType'] = self.scene_type
        result['BizId'] = self.biz_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.name = map.get('Name')
        self.catalog_id = map.get('CatalogId')
        self.id_number = map.get('IdNumber')
        self.face_url = map.get('FaceUrl')
        self.live_address = map.get('LiveAddress')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.scene_type = map.get('SceneType')
        self.biz_id = map.get('BizId')
        return self


class AddProfileResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: AddProfileResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AddProfileResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AddProfileResponseData(TeaModel):
    def __init__(self, live_address=None, scene_type=None, biz_id=None, face_url=None, gender=None, id_number=None,
                 isv_sub_id=None, phone_no=None, plate_no=None, catalog_id=None, profile_id=None, name=None):
        self.live_address = live_address  # type: str
        self.scene_type = scene_type    # type: str
        self.biz_id = biz_id            # type: str
        self.face_url = face_url        # type: str
        self.gender = gender            # type: str
        self.id_number = id_number      # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.phone_no = phone_no        # type: str
        self.plate_no = plate_no        # type: str
        self.catalog_id = catalog_id    # type: int
        self.profile_id = profile_id    # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.live_address, 'live_address')
        self.validate_required(self.scene_type, 'scene_type')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.face_url, 'face_url')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.phone_no, 'phone_no')
        self.validate_required(self.plate_no, 'plate_no')
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.profile_id, 'profile_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['LiveAddress'] = self.live_address
        result['SceneType'] = self.scene_type
        result['BizId'] = self.biz_id
        result['FaceUrl'] = self.face_url
        result['Gender'] = self.gender
        result['IdNumber'] = self.id_number
        result['IsvSubId'] = self.isv_sub_id
        result['PhoneNo'] = self.phone_no
        result['PlateNo'] = self.plate_no
        result['CatalogId'] = self.catalog_id
        result['ProfileId'] = self.profile_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.live_address = map.get('LiveAddress')
        self.scene_type = map.get('SceneType')
        self.biz_id = map.get('BizId')
        self.face_url = map.get('FaceUrl')
        self.gender = map.get('Gender')
        self.id_number = map.get('IdNumber')
        self.isv_sub_id = map.get('IsvSubId')
        self.phone_no = map.get('PhoneNo')
        self.plate_no = map.get('PlateNo')
        self.catalog_id = map.get('CatalogId')
        self.profile_id = map.get('ProfileId')
        self.name = map.get('Name')
        return self


class UpdateProfileCatalogRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, catalog_id=None, catalog_name=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.catalog_id = catalog_id    # type: int
        self.catalog_name = catalog_name  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.catalog_name, 'catalog_name')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['CatalogId'] = self.catalog_id
        result['CatalogName'] = self.catalog_name
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.catalog_id = map.get('CatalogId')
        self.catalog_name = map.get('CatalogName')
        return self


class UpdateProfileCatalogResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: UpdateProfileCatalogResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = UpdateProfileCatalogResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class UpdateProfileCatalogResponseData(TeaModel):
    def __init__(self, isv_sub_id=None, parent_catalog_id=None, profile_count=None, catalog_id=None,
                 catalog_name=None):
        self.isv_sub_id = isv_sub_id    # type: str
        self.parent_catalog_id = parent_catalog_id  # type: str
        self.profile_count = profile_count  # type: int
        self.catalog_id = catalog_id    # type: int
        self.catalog_name = catalog_name  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.parent_catalog_id, 'parent_catalog_id')
        self.validate_required(self.profile_count, 'profile_count')
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.catalog_name, 'catalog_name')

    def to_map(self):
        result = {}
        result['IsvSubId'] = self.isv_sub_id
        result['ParentCatalogId'] = self.parent_catalog_id
        result['ProfileCount'] = self.profile_count
        result['CatalogId'] = self.catalog_id
        result['CatalogName'] = self.catalog_name
        return result

    def from_map(self, map={}):
        self.isv_sub_id = map.get('IsvSubId')
        self.parent_catalog_id = map.get('ParentCatalogId')
        self.profile_count = map.get('ProfileCount')
        self.catalog_id = map.get('CatalogId')
        self.catalog_name = map.get('CatalogName')
        return self


class AddProfileCatalogRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, catalog_name=None, parent_catalog_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.catalog_name = catalog_name  # type: str
        self.parent_catalog_id = parent_catalog_id  # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.catalog_name, 'catalog_name')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['CatalogName'] = self.catalog_name
        result['ParentCatalogId'] = self.parent_catalog_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.catalog_name = map.get('CatalogName')
        self.parent_catalog_id = map.get('ParentCatalogId')
        return self


class AddProfileCatalogResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: AddProfileCatalogResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AddProfileCatalogResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AddProfileCatalogResponseData(TeaModel):
    def __init__(self, catalog_id=None, catalog_name=None, isv_sub_id=None):
        self.catalog_id = catalog_id    # type: int
        self.catalog_name = catalog_name  # type: str
        self.isv_sub_id = isv_sub_id    # type: str

    def validate(self):
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.catalog_name, 'catalog_name')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')

    def to_map(self):
        result = {}
        result['CatalogId'] = self.catalog_id
        result['CatalogName'] = self.catalog_name
        result['IsvSubId'] = self.isv_sub_id
        return result

    def from_map(self, map={}):
        self.catalog_id = map.get('CatalogId')
        self.catalog_name = map.get('CatalogName')
        self.isv_sub_id = map.get('IsvSubId')
        return self


class GetCatalogListRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        return self


class GetCatalogListResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetCatalogListResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetCatalogListResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetCatalogListResponseData(TeaModel):
    def __init__(self, isv_sub_id=None, parent_catalog_id=None, profile_count=None, catalog_id=None,
                 catalog_name=None):
        self.isv_sub_id = isv_sub_id    # type: str
        self.parent_catalog_id = parent_catalog_id  # type: int
        self.profile_count = profile_count  # type: int
        self.catalog_id = catalog_id    # type: int
        self.catalog_name = catalog_name  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.parent_catalog_id, 'parent_catalog_id')
        self.validate_required(self.profile_count, 'profile_count')
        self.validate_required(self.catalog_id, 'catalog_id')
        self.validate_required(self.catalog_name, 'catalog_name')

    def to_map(self):
        result = {}
        result['IsvSubId'] = self.isv_sub_id
        result['ParentCatalogId'] = self.parent_catalog_id
        result['ProfileCount'] = self.profile_count
        result['CatalogId'] = self.catalog_id
        result['CatalogName'] = self.catalog_name
        return result

    def from_map(self, map={}):
        self.isv_sub_id = map.get('IsvSubId')
        self.parent_catalog_id = map.get('ParentCatalogId')
        self.profile_count = map.get('ProfileCount')
        self.catalog_id = map.get('CatalogId')
        self.catalog_name = map.get('CatalogName')
        return self


class DeleteProfileRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, profile_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.profile_id = profile_id    # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.profile_id, 'profile_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['ProfileId'] = self.profile_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.profile_id = map.get('ProfileId')
        return self


class DeleteProfileResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: bool
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class UnbindCorpGroupRequest(TeaModel):
    def __init__(self, corp_id=None, corp_group_id=None):
        self.corp_id = corp_id          # type: str
        self.corp_group_id = corp_group_id  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.corp_group_id, 'corp_group_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['CorpGroupId'] = self.corp_group_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.corp_group_id = map.get('CorpGroupId')
        return self


class UnbindCorpGroupResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class BindCorpGroupRequest(TeaModel):
    def __init__(self, corp_id=None, corp_group_id=None):
        self.corp_id = corp_id          # type: str
        self.corp_group_id = corp_group_id  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.corp_group_id, 'corp_group_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['CorpGroupId'] = self.corp_group_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.corp_group_id = map.get('CorpGroupId')
        return self


class BindCorpGroupResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        return self


class ListUserGroupsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: List[ListUserGroupsResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListUserGroupsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListUserGroupsResponseData(TeaModel):
    def __init__(self, creator=None, user_group_name=None, isv_sub_id=None, user_group_id=None, user_count=None,
                 create_time=None, update_time=None, parent_user_group_id=None):
        self.creator = creator          # type: str
        self.user_group_name = user_group_name  # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_group_id = user_group_id  # type: int
        self.user_count = user_count    # type: int
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.parent_user_group_id = parent_user_group_id  # type: int

    def validate(self):
        self.validate_required(self.creator, 'creator')
        self.validate_required(self.user_group_name, 'user_group_name')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.user_count, 'user_count')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.parent_user_group_id, 'parent_user_group_id')

    def to_map(self):
        result = {}
        result['Creator'] = self.creator
        result['UserGroupName'] = self.user_group_name
        result['IsvSubId'] = self.isv_sub_id
        result['UserGroupId'] = self.user_group_id
        result['UserCount'] = self.user_count
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        result['ParentUserGroupId'] = self.parent_user_group_id
        return result

    def from_map(self, map={}):
        self.creator = map.get('Creator')
        self.user_group_name = map.get('UserGroupName')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_group_id = map.get('UserGroupId')
        self.user_count = map.get('UserCount')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        self.parent_user_group_id = map.get('ParentUserGroupId')
        return self


class GetPersonListRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, face_url=None, corp_id_list=None,
                 face_matching_rate_threshold=None, corp_id=None, person_id_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.face_url = face_url        # type: str
        self.corp_id_list = corp_id_list  # type: Dict[str, Any]
        self.face_matching_rate_threshold = face_matching_rate_threshold  # type: str
        self.corp_id = corp_id          # type: str
        self.person_id_list = person_id_list  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['FaceUrl'] = self.face_url
        result['CorpIdList'] = self.corp_id_list
        result['FaceMatchingRateThreshold'] = self.face_matching_rate_threshold
        result['CorpId'] = self.corp_id
        result['PersonIdList'] = self.person_id_list
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.face_url = map.get('FaceUrl')
        self.corp_id_list = map.get('CorpIdList')
        self.face_matching_rate_threshold = map.get('FaceMatchingRateThreshold')
        self.corp_id = map.get('CorpId')
        self.person_id_list = map.get('PersonIdList')
        return self


class GetPersonListShrinkRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, face_url=None, corp_id_list_shrink=None,
                 face_matching_rate_threshold=None, corp_id=None, person_id_list_shrink=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.face_url = face_url        # type: str
        self.corp_id_list_shrink = corp_id_list_shrink  # type: str
        self.face_matching_rate_threshold = face_matching_rate_threshold  # type: str
        self.corp_id = corp_id          # type: str
        self.person_id_list_shrink = person_id_list_shrink  # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['FaceUrl'] = self.face_url
        result['CorpIdList'] = self.corp_id_list_shrink
        result['FaceMatchingRateThreshold'] = self.face_matching_rate_threshold
        result['CorpId'] = self.corp_id
        result['PersonIdList'] = self.person_id_list_shrink
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.face_url = map.get('FaceUrl')
        self.corp_id_list_shrink = map.get('CorpIdList')
        self.face_matching_rate_threshold = map.get('FaceMatchingRateThreshold')
        self.corp_id = map.get('CorpId')
        self.person_id_list_shrink = map.get('PersonIdList')
        return self


class GetPersonListResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetPersonListResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetPersonListResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetPersonListResponseDataRecordsPropertyTagList(TeaModel):
    def __init__(self, code=None, tag_code_name=None, tag_name=None, value=None):
        self.code = code                # type: str
        self.tag_code_name = tag_code_name  # type: str
        self.tag_name = tag_name        # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.tag_code_name, 'tag_code_name')
        self.validate_required(self.tag_name, 'tag_name')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['TagCodeName'] = self.tag_code_name
        result['TagName'] = self.tag_name
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.tag_code_name = map.get('TagCodeName')
        self.tag_name = map.get('TagName')
        self.value = map.get('Value')
        return self


class GetPersonListResponseDataRecords(TeaModel):
    def __init__(self, face_url=None, first_shot_time=None, person_id=None, search_matching_rate=None,
                 last_shot_time=None, property_tag_list=None):
        self.face_url = face_url        # type: str
        self.first_shot_time = first_shot_time  # type: int
        self.person_id = person_id      # type: str
        self.search_matching_rate = search_matching_rate  # type: str
        self.last_shot_time = last_shot_time  # type: int
        self.property_tag_list = property_tag_list  # type: List[GetPersonListResponseDataRecordsPropertyTagList]

    def validate(self):
        self.validate_required(self.face_url, 'face_url')
        self.validate_required(self.first_shot_time, 'first_shot_time')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.search_matching_rate, 'search_matching_rate')
        self.validate_required(self.last_shot_time, 'last_shot_time')
        self.validate_required(self.property_tag_list, 'property_tag_list')
        if self.property_tag_list:
            for k in self.property_tag_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FaceUrl'] = self.face_url
        result['FirstShotTime'] = self.first_shot_time
        result['PersonId'] = self.person_id
        result['SearchMatchingRate'] = self.search_matching_rate
        result['LastShotTime'] = self.last_shot_time
        result['PropertyTagList'] = []
        if self.property_tag_list is not None:
            for k in self.property_tag_list:
                result['PropertyTagList'].append(k.to_map() if k else None)
        else:
            result['PropertyTagList'] = None
        return result

    def from_map(self, map={}):
        self.face_url = map.get('FaceUrl')
        self.first_shot_time = map.get('FirstShotTime')
        self.person_id = map.get('PersonId')
        self.search_matching_rate = map.get('SearchMatchingRate')
        self.last_shot_time = map.get('LastShotTime')
        self.property_tag_list = []
        if map.get('PropertyTagList') is not None:
            for k in map.get('PropertyTagList'):
                temp_model = GetPersonListResponseDataRecordsPropertyTagList()
                self.property_tag_list.append(temp_model.from_map(k))
        else:
            self.property_tag_list = None
        return self


class GetPersonListResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.records = records          # type: List[GetPersonListResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = GetPersonListResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_name=None, user_group_id=None, id_number=None,
                 face_image_url=None, address=None, age=None, gender=None, plate_no=None, phone_no=None, attachment=None,
                 biz_id=None, page_number=None, page_size=None, person_list=None, user_list=None,
                 matching_rate_threshold=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_name = user_name      # type: str
        self.user_group_id = user_group_id  # type: int
        self.id_number = id_number      # type: str
        self.face_image_url = face_image_url  # type: str
        self.address = address          # type: str
        self.age = age                  # type: int
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.attachment = attachment    # type: str
        self.biz_id = biz_id            # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.person_list = person_list  # type: Dict[str, Any]
        self.user_list = user_list      # type: Dict[str, Any]
        self.matching_rate_threshold = matching_rate_threshold  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserName'] = self.user_name
        result['UserGroupId'] = self.user_group_id
        result['IdNumber'] = self.id_number
        result['FaceImageUrl'] = self.face_image_url
        result['Address'] = self.address
        result['Age'] = self.age
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['Attachment'] = self.attachment
        result['BizId'] = self.biz_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['PersonList'] = self.person_list
        result['UserList'] = self.user_list
        result['MatchingRateThreshold'] = self.matching_rate_threshold
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_name = map.get('UserName')
        self.user_group_id = map.get('UserGroupId')
        self.id_number = map.get('IdNumber')
        self.face_image_url = map.get('FaceImageUrl')
        self.address = map.get('Address')
        self.age = map.get('Age')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.attachment = map.get('Attachment')
        self.biz_id = map.get('BizId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.person_list = map.get('PersonList')
        self.user_list = map.get('UserList')
        self.matching_rate_threshold = map.get('MatchingRateThreshold')
        return self


class ListUsersShrinkRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_name=None, user_group_id=None, id_number=None,
                 face_image_url=None, address=None, age=None, gender=None, plate_no=None, phone_no=None, attachment=None,
                 biz_id=None, page_number=None, page_size=None, person_list_shrink=None, user_list_shrink=None,
                 matching_rate_threshold=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_name = user_name      # type: str
        self.user_group_id = user_group_id  # type: int
        self.id_number = id_number      # type: str
        self.face_image_url = face_image_url  # type: str
        self.address = address          # type: str
        self.age = age                  # type: int
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.attachment = attachment    # type: str
        self.biz_id = biz_id            # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.person_list_shrink = person_list_shrink  # type: str
        self.user_list_shrink = user_list_shrink  # type: str
        self.matching_rate_threshold = matching_rate_threshold  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserName'] = self.user_name
        result['UserGroupId'] = self.user_group_id
        result['IdNumber'] = self.id_number
        result['FaceImageUrl'] = self.face_image_url
        result['Address'] = self.address
        result['Age'] = self.age
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['Attachment'] = self.attachment
        result['BizId'] = self.biz_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['PersonList'] = self.person_list_shrink
        result['UserList'] = self.user_list_shrink
        result['MatchingRateThreshold'] = self.matching_rate_threshold
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_name = map.get('UserName')
        self.user_group_id = map.get('UserGroupId')
        self.id_number = map.get('IdNumber')
        self.face_image_url = map.get('FaceImageUrl')
        self.address = map.get('Address')
        self.age = map.get('Age')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.attachment = map.get('Attachment')
        self.biz_id = map.get('BizId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.person_list_shrink = map.get('PersonList')
        self.user_list_shrink = map.get('UserList')
        self.matching_rate_threshold = map.get('MatchingRateThreshold')
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListUsersResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListUsersResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListUsersResponseDataRecords(TeaModel):
    def __init__(self, user_group_id=None, age=None, attachment=None, biz_id=None, face_image_url=None, gender=None,
                 id_number=None, user_id=None, user_name=None, isv_sub_id=None, matching_rate=None, person_id=None):
        self.user_group_id = user_group_id  # type: int
        self.age = age                  # type: str
        self.attachment = attachment    # type: str
        self.biz_id = biz_id            # type: str
        self.face_image_url = face_image_url  # type: str
        self.gender = gender            # type: str
        self.id_number = id_number      # type: str
        self.user_id = user_id          # type: int
        self.user_name = user_name      # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.matching_rate = matching_rate  # type: str
        self.person_id = person_id      # type: str

    def validate(self):
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.age, 'age')
        self.validate_required(self.attachment, 'attachment')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.matching_rate, 'matching_rate')
        self.validate_required(self.person_id, 'person_id')

    def to_map(self):
        result = {}
        result['UserGroupId'] = self.user_group_id
        result['Age'] = self.age
        result['Attachment'] = self.attachment
        result['BizId'] = self.biz_id
        result['FaceImageUrl'] = self.face_image_url
        result['Gender'] = self.gender
        result['IdNumber'] = self.id_number
        result['UserId'] = self.user_id
        result['UserName'] = self.user_name
        result['IsvSubId'] = self.isv_sub_id
        result['MatchingRate'] = self.matching_rate
        result['PersonId'] = self.person_id
        return result

    def from_map(self, map={}):
        self.user_group_id = map.get('UserGroupId')
        self.age = map.get('Age')
        self.attachment = map.get('Attachment')
        self.biz_id = map.get('BizId')
        self.face_image_url = map.get('FaceImageUrl')
        self.gender = map.get('Gender')
        self.id_number = map.get('IdNumber')
        self.user_id = map.get('UserId')
        self.user_name = map.get('UserName')
        self.isv_sub_id = map.get('IsvSubId')
        self.matching_rate = map.get('MatchingRate')
        self.person_id = map.get('PersonId')
        return self


class ListUsersResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, success=None, total=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.success = success          # type: int
        self.total = total              # type: int
        self.records = records          # type: List[ListUsersResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.success, 'success')
        self.validate_required(self.total, 'total')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Success'] = self.success
        result['Total'] = self.total
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.success = map.get('Success')
        self.total = map.get('Total')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListUsersResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_name=None, user_group_id=None, id_number=None,
                 face_image_url=None, address=None, age=None, gender=None, plate_no=None, phone_no=None, attachment=None,
                 biz_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_name = user_name      # type: str
        self.user_group_id = user_group_id  # type: int
        self.id_number = id_number      # type: str
        self.face_image_url = face_image_url  # type: str
        self.address = address          # type: str
        self.age = age                  # type: int
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.attachment = attachment    # type: str
        self.biz_id = biz_id            # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.user_group_id, 'user_group_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserName'] = self.user_name
        result['UserGroupId'] = self.user_group_id
        result['IdNumber'] = self.id_number
        result['FaceImageUrl'] = self.face_image_url
        result['Address'] = self.address
        result['Age'] = self.age
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['Attachment'] = self.attachment
        result['BizId'] = self.biz_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_name = map.get('UserName')
        self.user_group_id = map.get('UserGroupId')
        self.id_number = map.get('IdNumber')
        self.face_image_url = map.get('FaceImageUrl')
        self.address = map.get('Address')
        self.age = map.get('Age')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.attachment = map.get('Attachment')
        self.biz_id = map.get('BizId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: CreateUserResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = CreateUserResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CreateUserResponseData(TeaModel):
    def __init__(self, user_id=None, isv_sub_id=None, user_name=None, user_group_id=None, id_number=None,
                 face_image_url=None, address=None, age=None, gender=None, plate_no=None, phone_no=None, attachment=None,
                 biz_id=None):
        self.user_id = user_id          # type: int
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_name = user_name      # type: str
        self.user_group_id = user_group_id  # type: int
        self.id_number = id_number      # type: str
        self.face_image_url = face_image_url  # type: str
        self.address = address          # type: str
        self.age = age                  # type: str
        self.gender = gender            # type: str
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.attachment = attachment    # type: str
        self.biz_id = biz_id            # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.address, 'address')
        self.validate_required(self.age, 'age')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.plate_no, 'plate_no')
        self.validate_required(self.phone_no, 'phone_no')
        self.validate_required(self.attachment, 'attachment')
        self.validate_required(self.biz_id, 'biz_id')

    def to_map(self):
        result = {}
        result['UserId'] = self.user_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserName'] = self.user_name
        result['UserGroupId'] = self.user_group_id
        result['IdNumber'] = self.id_number
        result['FaceImageUrl'] = self.face_image_url
        result['Address'] = self.address
        result['Age'] = self.age
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['Attachment'] = self.attachment
        result['BizId'] = self.biz_id
        return result

    def from_map(self, map={}):
        self.user_id = map.get('UserId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_name = map.get('UserName')
        self.user_group_id = map.get('UserGroupId')
        self.id_number = map.get('IdNumber')
        self.face_image_url = map.get('FaceImageUrl')
        self.address = map.get('Address')
        self.age = map.get('Age')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.attachment = map.get('Attachment')
        self.biz_id = map.get('BizId')
        return self


class BindUserRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, matching_rate=None, person_id=None, user_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.matching_rate = matching_rate  # type: str
        self.person_id = person_id      # type: str
        self.user_id = user_id          # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.matching_rate, 'matching_rate')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['MatchingRate'] = self.matching_rate
        result['PersonId'] = self.person_id
        result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.matching_rate = map.get('MatchingRate')
        self.person_id = map.get('PersonId')
        self.user_id = map.get('UserId')
        return self


class BindUserResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: bool
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class GetUserDetailRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_id=None, need_face_detail=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_id = user_id          # type: int
        self.need_face_detail = need_face_detail  # type: bool

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserId'] = self.user_id
        result['NeedFaceDetail'] = self.need_face_detail
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_id = map.get('UserId')
        self.need_face_detail = map.get('NeedFaceDetail')
        return self


class GetUserDetailResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetUserDetailResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetUserDetailResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetUserDetailResponseData(TeaModel):
    def __init__(self, address=None, age=None, attachment=None, biz_id=None, face_image_url=None, gender=None,
                 id_number=None, phone_no=None, plate_no=None, user_group_id=None, user_id=None, user_name=None,
                 isv_sub_id=None):
        self.address = address          # type: str
        self.age = age                  # type: str
        self.attachment = attachment    # type: str
        self.biz_id = biz_id            # type: str
        self.face_image_url = face_image_url  # type: str
        self.gender = gender            # type: str
        self.id_number = id_number      # type: str
        self.phone_no = phone_no        # type: str
        self.plate_no = plate_no        # type: str
        self.user_group_id = user_group_id  # type: int
        self.user_id = user_id          # type: int
        self.user_name = user_name      # type: str
        self.isv_sub_id = isv_sub_id    # type: str

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.age, 'age')
        self.validate_required(self.attachment, 'attachment')
        self.validate_required(self.biz_id, 'biz_id')
        self.validate_required(self.face_image_url, 'face_image_url')
        self.validate_required(self.gender, 'gender')
        self.validate_required(self.id_number, 'id_number')
        self.validate_required(self.phone_no, 'phone_no')
        self.validate_required(self.plate_no, 'plate_no')
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')

    def to_map(self):
        result = {}
        result['Address'] = self.address
        result['Age'] = self.age
        result['Attachment'] = self.attachment
        result['BizId'] = self.biz_id
        result['FaceImageUrl'] = self.face_image_url
        result['Gender'] = self.gender
        result['IdNumber'] = self.id_number
        result['PhoneNo'] = self.phone_no
        result['PlateNo'] = self.plate_no
        result['UserGroupId'] = self.user_group_id
        result['UserId'] = self.user_id
        result['UserName'] = self.user_name
        result['IsvSubId'] = self.isv_sub_id
        return result

    def from_map(self, map={}):
        self.address = map.get('Address')
        self.age = map.get('Age')
        self.attachment = map.get('Attachment')
        self.biz_id = map.get('BizId')
        self.face_image_url = map.get('FaceImageUrl')
        self.gender = map.get('Gender')
        self.id_number = map.get('IdNumber')
        self.phone_no = map.get('PhoneNo')
        self.plate_no = map.get('PlateNo')
        self.user_group_id = map.get('UserGroupId')
        self.user_id = map.get('UserId')
        self.user_name = map.get('UserName')
        self.isv_sub_id = map.get('IsvSubId')
        return self


class UploadImageRequest(TeaModel):
    def __init__(self, image_url=None):
        self.image_url = image_url      # type: str

    def validate(self):
        self.validate_required(self.image_url, 'image_url')

    def to_map(self):
        result = {}
        result['ImageUrl'] = self.image_url
        return result

    def from_map(self, map={}):
        self.image_url = map.get('ImageUrl')
        return self


class UploadImageResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class UpdateUserGroupRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_group_id=None, user_group_name=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_group_id = user_group_id  # type: int
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.user_group_name, 'user_group_name')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserGroupId'] = self.user_group_id
        result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_group_id = map.get('UserGroupId')
        self.user_group_name = map.get('UserGroupName')
        return self


class UpdateUserGroupResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: UpdateUserGroupResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = UpdateUserGroupResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class UpdateUserGroupResponseData(TeaModel):
    def __init__(self, user_group_id=None, isv_sub_id=None, user_group_name=None, user_count=None,
                 parent_user_group_id=None):
        self.user_group_id = user_group_id  # type: int
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_group_name = user_group_name  # type: str
        self.user_count = user_count    # type: int
        self.parent_user_group_id = parent_user_group_id  # type: str

    def validate(self):
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_group_name, 'user_group_name')
        self.validate_required(self.user_count, 'user_count')
        self.validate_required(self.parent_user_group_id, 'parent_user_group_id')

    def to_map(self):
        result = {}
        result['UserGroupId'] = self.user_group_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserGroupName'] = self.user_group_name
        result['UserCount'] = self.user_count
        result['ParentUserGroupId'] = self.parent_user_group_id
        return result

    def from_map(self, map={}):
        self.user_group_id = map.get('UserGroupId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_group_name = map.get('UserGroupName')
        self.user_count = map.get('UserCount')
        self.parent_user_group_id = map.get('ParentUserGroupId')
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_group_name=None, parent_user_group_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_group_name = user_group_name  # type: str
        self.parent_user_group_id = parent_user_group_id  # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_group_name, 'user_group_name')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserGroupName'] = self.user_group_name
        result['ParentUserGroupId'] = self.parent_user_group_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_group_name = map.get('UserGroupName')
        self.parent_user_group_id = map.get('ParentUserGroupId')
        return self


class CreateUserGroupResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: CreateUserGroupResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = CreateUserGroupResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class CreateUserGroupResponseData(TeaModel):
    def __init__(self, user_group_name=None, isv_sub_id=None, user_group_id=None):
        self.user_group_name = user_group_name  # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_group_id = user_group_id  # type: int

    def validate(self):
        self.validate_required(self.user_group_name, 'user_group_name')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_group_id, 'user_group_id')

    def to_map(self):
        result = {}
        result['UserGroupName'] = self.user_group_name
        result['IsvSubId'] = self.isv_sub_id
        result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, map={}):
        self.user_group_name = map.get('UserGroupName')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_group_id = map.get('UserGroupId')
        return self


class UnbindUserRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_id = user_id          # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_id = map.get('UserId')
        return self


class UnbindUserResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: bool
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class UpdateUserRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_name=None, user_group_id=None, id_number=None,
                 face_image_url=None, face_image_content=None, address=None, age=None, gender=None, plate_no=None, phone_no=None,
                 attachment=None, biz_id=None, user_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_name = user_name      # type: str
        self.user_group_id = user_group_id  # type: int
        self.id_number = id_number      # type: str
        self.face_image_url = face_image_url  # type: str
        self.face_image_content = face_image_content  # type: str
        self.address = address          # type: str
        self.age = age                  # type: int
        self.gender = gender            # type: int
        self.plate_no = plate_no        # type: str
        self.phone_no = phone_no        # type: str
        self.attachment = attachment    # type: str
        self.biz_id = biz_id            # type: str
        self.user_id = user_id          # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserName'] = self.user_name
        result['UserGroupId'] = self.user_group_id
        result['IdNumber'] = self.id_number
        result['FaceImageUrl'] = self.face_image_url
        result['FaceImageContent'] = self.face_image_content
        result['Address'] = self.address
        result['Age'] = self.age
        result['Gender'] = self.gender
        result['PlateNo'] = self.plate_no
        result['PhoneNo'] = self.phone_no
        result['Attachment'] = self.attachment
        result['BizId'] = self.biz_id
        result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_name = map.get('UserName')
        self.user_group_id = map.get('UserGroupId')
        self.id_number = map.get('IdNumber')
        self.face_image_url = map.get('FaceImageUrl')
        self.face_image_content = map.get('FaceImageContent')
        self.address = map.get('Address')
        self.age = map.get('Age')
        self.gender = map.get('Gender')
        self.plate_no = map.get('PlateNo')
        self.phone_no = map.get('PhoneNo')
        self.attachment = map.get('Attachment')
        self.biz_id = map.get('BizId')
        self.user_id = map.get('UserId')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_id = user_id          # type: int

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_id = map.get('UserId')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: bool
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(self, corp_id=None, isv_sub_id=None, user_group_id=None):
        self.corp_id = corp_id          # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.user_group_id, 'user_group_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['IsvSubId'] = self.isv_sub_id
        result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.isv_sub_id = map.get('IsvSubId')
        self.user_group_id = map.get('UserGroupId')
        return self


class DeleteUserGroupResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: bool

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class ListPersonVisitCountRequest(TeaModel):
    def __init__(self, corp_id=None, page_number=None, page_size=None, start_time=None, end_time=None,
                 aggregate_type=None, tag_code=None, time_aggregate_type=None, min_val=None, max_val=None, count_type=None):
        self.corp_id = corp_id          # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.aggregate_type = aggregate_type  # type: str
        self.tag_code = tag_code        # type: str
        self.time_aggregate_type = time_aggregate_type  # type: str
        self.min_val = min_val          # type: int
        self.max_val = max_val          # type: int
        self.count_type = count_type    # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.aggregate_type, 'aggregate_type')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.time_aggregate_type, 'time_aggregate_type')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['AggregateType'] = self.aggregate_type
        result['TagCode'] = self.tag_code
        result['TimeAggregateType'] = self.time_aggregate_type
        result['MinVal'] = self.min_val
        result['MaxVal'] = self.max_val
        result['CountType'] = self.count_type
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.aggregate_type = map.get('AggregateType')
        self.tag_code = map.get('TagCode')
        self.time_aggregate_type = map.get('TimeAggregateType')
        self.min_val = map.get('MinVal')
        self.max_val = map.get('MaxVal')
        self.count_type = map.get('CountType')
        return self


class ListPersonVisitCountResponse(TeaModel):
    def __init__(self, code=None, message=None, page_no=None, page_size=None, request_id=None, success=None,
                 total_count=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.page_no = page_no          # type: str
        self.page_size = page_size      # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.total_count = total_count  # type: str
        self.data = data                # type: List[ListPersonVisitCountResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.total_count = map.get('TotalCount')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListPersonVisitCountResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListPersonVisitCountResponseData(TeaModel):
    def __init__(self, corp_id=None, device_id=None, group_id=None, person_id=None, tag_code=None, tag_metrics=None,
                 hour_id=None, day_id=None):
        self.corp_id = corp_id          # type: str
        self.device_id = device_id      # type: str
        self.group_id = group_id        # type: str
        self.person_id = person_id      # type: str
        self.tag_code = tag_code        # type: str
        self.tag_metrics = tag_metrics  # type: str
        self.hour_id = hour_id          # type: str
        self.day_id = day_id            # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.tag_metrics, 'tag_metrics')
        self.validate_required(self.hour_id, 'hour_id')
        self.validate_required(self.day_id, 'day_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['DeviceId'] = self.device_id
        result['GroupId'] = self.group_id
        result['PersonId'] = self.person_id
        result['TagCode'] = self.tag_code
        result['TagMetrics'] = self.tag_metrics
        result['HourId'] = self.hour_id
        result['DayId'] = self.day_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.device_id = map.get('DeviceId')
        self.group_id = map.get('GroupId')
        self.person_id = map.get('PersonId')
        self.tag_code = map.get('TagCode')
        self.tag_metrics = map.get('TagMetrics')
        self.hour_id = map.get('HourId')
        self.day_id = map.get('DayId')
        return self


class ListEventAlgorithmDetailsRequest(TeaModel):
    def __init__(self, corp_id=None, event_type=None, data_source_id=None, start_time=None, end_time=None,
                 page_number=None, page_size=None, source_id=None, record_id=None, event_value=None, extend_value=None):
        self.corp_id = corp_id          # type: str
        self.event_type = event_type    # type: str
        self.data_source_id = data_source_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.source_id = source_id      # type: str
        self.record_id = record_id      # type: str
        self.event_value = event_value  # type: str
        self.extend_value = extend_value  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['EventType'] = self.event_type
        result['DataSourceId'] = self.data_source_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['SourceId'] = self.source_id
        result['RecordId'] = self.record_id
        result['EventValue'] = self.event_value
        result['ExtendValue'] = self.extend_value
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.event_type = map.get('EventType')
        self.data_source_id = map.get('DataSourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.source_id = map.get('SourceId')
        self.record_id = map.get('RecordId')
        self.event_value = map.get('EventValue')
        self.extend_value = map.get('ExtendValue')
        return self


class ListEventAlgorithmDetailsResponse(TeaModel):
    def __init__(self, code=None, message=None, page_number=None, page_size=None, request_id=None, success=None,
                 total_count=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.total_count = total_count  # type: int
        self.data = data                # type: List[ListEventAlgorithmDetailsResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.total_count = map.get('TotalCount')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListEventAlgorithmDetailsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListEventAlgorithmDetailsResponseData(TeaModel):
    def __init__(self, corp_id=None, data_source_id=None, event_type=None, event_value=None, extend_value=None,
                 extra_extend_value=None, face_count=None, left_top_x=None, left_top_y=None, pic_url_path=None, point_x=None,
                 point_y=None, record_id=None, right_bottom_x=None, right_bottom_y=None, shot_time=None, source_id=None,
                 target_pic_url_path=None):
        self.corp_id = corp_id          # type: str
        self.data_source_id = data_source_id  # type: str
        self.event_type = event_type    # type: str
        self.event_value = event_value  # type: str
        self.extend_value = extend_value  # type: str
        self.extra_extend_value = extra_extend_value  # type: str
        self.face_count = face_count    # type: str
        self.left_top_x = left_top_x    # type: str
        self.left_top_y = left_top_y    # type: str
        self.pic_url_path = pic_url_path  # type: str
        self.point_x = point_x          # type: str
        self.point_y = point_y          # type: str
        self.record_id = record_id      # type: str
        self.right_bottom_x = right_bottom_x  # type: str
        self.right_bottom_y = right_bottom_y  # type: str
        self.shot_time = shot_time      # type: str
        self.source_id = source_id      # type: str
        self.target_pic_url_path = target_pic_url_path  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.data_source_id, 'data_source_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.event_value, 'event_value')
        self.validate_required(self.extend_value, 'extend_value')
        self.validate_required(self.extra_extend_value, 'extra_extend_value')
        self.validate_required(self.face_count, 'face_count')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.pic_url_path, 'pic_url_path')
        self.validate_required(self.point_x, 'point_x')
        self.validate_required(self.point_y, 'point_y')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.source_id, 'source_id')
        self.validate_required(self.target_pic_url_path, 'target_pic_url_path')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['DataSourceId'] = self.data_source_id
        result['EventType'] = self.event_type
        result['EventValue'] = self.event_value
        result['ExtendValue'] = self.extend_value
        result['ExtraExtendValue'] = self.extra_extend_value
        result['FaceCount'] = self.face_count
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['PicUrlPath'] = self.pic_url_path
        result['PointX'] = self.point_x
        result['PointY'] = self.point_y
        result['RecordId'] = self.record_id
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['ShotTime'] = self.shot_time
        result['SourceId'] = self.source_id
        result['TargetPicUrlPath'] = self.target_pic_url_path
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.data_source_id = map.get('DataSourceId')
        self.event_type = map.get('EventType')
        self.event_value = map.get('EventValue')
        self.extend_value = map.get('ExtendValue')
        self.extra_extend_value = map.get('ExtraExtendValue')
        self.face_count = map.get('FaceCount')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.pic_url_path = map.get('PicUrlPath')
        self.point_x = map.get('PointX')
        self.point_y = map.get('PointY')
        self.record_id = map.get('RecordId')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.shot_time = map.get('ShotTime')
        self.source_id = map.get('SourceId')
        self.target_pic_url_path = map.get('TargetPicUrlPath')
        return self


class ListCorpMetricsRequest(TeaModel):
    def __init__(self, corp_id=None, tag_code=None, start_time=None, end_time=None, page_number=None, page_size=None,
                 user_group_list=None, device_group_list=None, device_id_list=None):
        self.corp_id = corp_id          # type: str
        self.tag_code = tag_code        # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.user_group_list = user_group_list  # type: str
        self.device_group_list = device_group_list  # type: str
        self.device_id_list = device_id_list  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TagCode'] = self.tag_code
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['UserGroupList'] = self.user_group_list
        result['DeviceGroupList'] = self.device_group_list
        result['DeviceIdList'] = self.device_id_list
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.tag_code = map.get('TagCode')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.user_group_list = map.get('UserGroupList')
        self.device_group_list = map.get('DeviceGroupList')
        self.device_id_list = map.get('DeviceIdList')
        return self


class ListCorpMetricsResponse(TeaModel):
    def __init__(self, code=None, message=None, page_number=None, page_size=None, request_id=None, success=None,
                 total_count=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.total_count = total_count  # type: int
        self.data = data                # type: List[ListCorpMetricsResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.total_count = map.get('TotalCount')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListCorpMetricsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListCorpMetricsResponseData(TeaModel):
    def __init__(self, corp_id=None, tag_code=None, tag_metrics=None, tag_value=None, device_group_id=None,
                 device_id=None, user_group_id=None, person_id=None, date_id=None):
        self.corp_id = corp_id          # type: str
        self.tag_code = tag_code        # type: str
        self.tag_metrics = tag_metrics  # type: str
        self.tag_value = tag_value      # type: str
        self.device_group_id = device_group_id  # type: str
        self.device_id = device_id      # type: str
        self.user_group_id = user_group_id  # type: str
        self.person_id = person_id      # type: str
        self.date_id = date_id          # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.tag_metrics, 'tag_metrics')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.device_group_id, 'device_group_id')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.date_id, 'date_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TagCode'] = self.tag_code
        result['TagMetrics'] = self.tag_metrics
        result['TagValue'] = self.tag_value
        result['DeviceGroupId'] = self.device_group_id
        result['DeviceId'] = self.device_id
        result['UserGroupId'] = self.user_group_id
        result['PersonId'] = self.person_id
        result['DateId'] = self.date_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.tag_code = map.get('TagCode')
        self.tag_metrics = map.get('TagMetrics')
        self.tag_value = map.get('TagValue')
        self.device_group_id = map.get('DeviceGroupId')
        self.device_id = map.get('DeviceId')
        self.user_group_id = map.get('UserGroupId')
        self.person_id = map.get('PersonId')
        self.date_id = map.get('DateId')
        return self


class ListPersonTraceRequest(TeaModel):
    def __init__(self, start_time=None, corp_id=None, page_number=None, page_size=None, end_time=None,
                 data_source_id=None, person_id=None, group_id=None):
        self.start_time = start_time    # type: str
        self.corp_id = corp_id          # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.end_time = end_time        # type: str
        self.data_source_id = data_source_id  # type: str
        self.person_id = person_id      # type: str
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['CorpId'] = self.corp_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['EndTime'] = self.end_time
        result['DataSourceId'] = self.data_source_id
        result['PersonId'] = self.person_id
        result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.corp_id = map.get('CorpId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.end_time = map.get('EndTime')
        self.data_source_id = map.get('DataSourceId')
        self.person_id = map.get('PersonId')
        self.group_id = map.get('GroupId')
        return self


class ListPersonTraceResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, total_count=None, page_size=None,
                 page_number=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: str
        self.total_count = total_count  # type: int
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.data = data                # type: List[ListPersonTraceResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['TotalCount'] = self.total_count
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.total_count = map.get('TotalCount')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListPersonTraceResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListPersonTraceResponseData(TeaModel):
    def __init__(self, date=None, last_time=None, start_time=None, end_source_image=None, device_id=None,
                 start_target_image=None, group_id=None, person_id=None, start_source_image=None, corp_id=None, end_target_image=None):
        self.date = date                # type: str
        self.last_time = last_time      # type: str
        self.start_time = start_time    # type: str
        self.end_source_image = end_source_image  # type: str
        self.device_id = device_id      # type: str
        self.start_target_image = start_target_image  # type: str
        self.group_id = group_id        # type: str
        self.person_id = person_id      # type: str
        self.start_source_image = start_source_image  # type: str
        self.corp_id = corp_id          # type: str
        self.end_target_image = end_target_image  # type: str

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.last_time, 'last_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_source_image, 'end_source_image')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.start_target_image, 'start_target_image')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.start_source_image, 'start_source_image')
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.end_target_image, 'end_target_image')

    def to_map(self):
        result = {}
        result['Date'] = self.date
        result['LastTime'] = self.last_time
        result['StartTime'] = self.start_time
        result['EndSourceImage'] = self.end_source_image
        result['DeviceId'] = self.device_id
        result['StartTargetImage'] = self.start_target_image
        result['GroupId'] = self.group_id
        result['PersonId'] = self.person_id
        result['StartSourceImage'] = self.start_source_image
        result['CorpId'] = self.corp_id
        result['EndTargetImage'] = self.end_target_image
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.last_time = map.get('LastTime')
        self.start_time = map.get('StartTime')
        self.end_source_image = map.get('EndSourceImage')
        self.device_id = map.get('DeviceId')
        self.start_target_image = map.get('StartTargetImage')
        self.group_id = map.get('GroupId')
        self.person_id = map.get('PersonId')
        self.start_source_image = map.get('StartSourceImage')
        self.corp_id = map.get('CorpId')
        self.end_target_image = map.get('EndTargetImage')
        return self


class ListCorpGroupMetricsRequest(TeaModel):
    def __init__(self, start_time=None, tag_code=None, end_time=None, group_id=None, page_number=None,
                 page_size=None, device_id=None, corp_id=None, user_group=None, device_group=None):
        self.start_time = start_time    # type: str
        self.tag_code = tag_code        # type: str
        self.end_time = end_time        # type: str
        self.group_id = group_id        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.device_id = device_id      # type: str
        self.corp_id = corp_id          # type: str
        self.user_group = user_group    # type: str
        self.device_group = device_group  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['TagCode'] = self.tag_code
        result['EndTime'] = self.end_time
        result['GroupId'] = self.group_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['DeviceId'] = self.device_id
        result['CorpId'] = self.corp_id
        result['UserGroup'] = self.user_group
        result['DeviceGroup'] = self.device_group
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.tag_code = map.get('TagCode')
        self.end_time = map.get('EndTime')
        self.group_id = map.get('GroupId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.device_id = map.get('DeviceId')
        self.corp_id = map.get('CorpId')
        self.user_group = map.get('UserGroup')
        self.device_group = map.get('DeviceGroup')
        return self


class ListCorpGroupMetricsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, page_number=None, page_size=None, total_count=None,
                 success=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.success = success          # type: str
        self.data = data                # type: List[ListCorpGroupMetricsResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Success'] = self.success
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.success = map.get('Success')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListCorpGroupMetricsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListCorpGroupMetricsResponseData(TeaModel):
    def __init__(self, date_id=None, tag_metrics=None, tag_code=None, tag_value=None, corp_group_id=None,
                 corp_id=None, device_group_id=None, device_id=None, user_group_id=None, person_id=None):
        self.date_id = date_id          # type: str
        self.tag_metrics = tag_metrics  # type: str
        self.tag_code = tag_code        # type: str
        self.tag_value = tag_value      # type: str
        self.corp_group_id = corp_group_id  # type: str
        self.corp_id = corp_id          # type: str
        self.device_group_id = device_group_id  # type: str
        self.device_id = device_id      # type: str
        self.user_group_id = user_group_id  # type: str
        self.person_id = person_id      # type: str

    def validate(self):
        self.validate_required(self.date_id, 'date_id')
        self.validate_required(self.tag_metrics, 'tag_metrics')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.corp_group_id, 'corp_group_id')
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.device_group_id, 'device_group_id')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.user_group_id, 'user_group_id')
        self.validate_required(self.person_id, 'person_id')

    def to_map(self):
        result = {}
        result['DateId'] = self.date_id
        result['TagMetrics'] = self.tag_metrics
        result['TagCode'] = self.tag_code
        result['TagValue'] = self.tag_value
        result['CorpGroupId'] = self.corp_group_id
        result['CorpId'] = self.corp_id
        result['DeviceGroupId'] = self.device_group_id
        result['DeviceId'] = self.device_id
        result['UserGroupId'] = self.user_group_id
        result['PersonID'] = self.person_id
        return result

    def from_map(self, map={}):
        self.date_id = map.get('DateId')
        self.tag_metrics = map.get('TagMetrics')
        self.tag_code = map.get('TagCode')
        self.tag_value = map.get('TagValue')
        self.corp_group_id = map.get('CorpGroupId')
        self.corp_id = map.get('CorpId')
        self.device_group_id = map.get('DeviceGroupId')
        self.device_id = map.get('DeviceId')
        self.user_group_id = map.get('UserGroupId')
        self.person_id = map.get('PersonID')
        return self


class GetFaceModelResultRequest(TeaModel):
    def __init__(self, picture_id=None, picture_content=None, picture_url=None):
        self.picture_id = picture_id    # type: str
        self.picture_content = picture_content  # type: str
        self.picture_url = picture_url  # type: str

    def validate(self):
        self.validate_required(self.picture_id, 'picture_id')

    def to_map(self):
        result = {}
        result['PictureId'] = self.picture_id
        result['PictureContent'] = self.picture_content
        result['PictureUrl'] = self.picture_url
        return result

    def from_map(self, map={}):
        self.picture_id = map.get('PictureId')
        self.picture_content = map.get('PictureContent')
        self.picture_url = map.get('PictureUrl')
        return self


class GetFaceModelResultResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetFaceModelResultResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetFaceModelResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetFaceModelResultResponseDataRecords(TeaModel):
    def __init__(self, mustache_style=None, face_style=None, cap_style=None, skin_color=None, right_bottom_y=None,
                 right_bottom_x=None, hair_style=None, gender_code=None, respirator_color=None, ethic_code=None,
                 age_lower_limit=None, left_top_y=None, left_top_x=None, hair_color=None, age_up_limit=None, glass_style=None,
                 glass_color=None, cap_color=None, cap_color_reliability=None, respirator_color_reliability=None,
                 ethic_code_reliability=None, gender_code_reliability=None, glass_color_reliability=None, skin_color_reliability=None,
                 mustache_style_reliability=None, cap_style_reliability=None, face_style_reliability=None, glass_style_reliability=None,
                 age_up_limit_reliability=None, hair_style_reliability=None, age_lower_limit_reliability=None, hair_color_reliability=None,
                 feature_data=None):
        self.mustache_style = mustache_style  # type: str
        self.face_style = face_style    # type: str
        self.cap_style = cap_style      # type: int
        self.skin_color = skin_color    # type: int
        self.right_bottom_y = right_bottom_y  # type: float
        self.right_bottom_x = right_bottom_x  # type: float
        self.hair_style = hair_style    # type: int
        self.gender_code = gender_code  # type: int
        self.respirator_color = respirator_color  # type: int
        self.ethic_code = ethic_code    # type: int
        self.age_lower_limit = age_lower_limit  # type: int
        self.left_top_y = left_top_y    # type: float
        self.left_top_x = left_top_x    # type: float
        self.hair_color = hair_color    # type: int
        self.age_up_limit = age_up_limit  # type: int
        self.glass_style = glass_style  # type: int
        self.glass_color = glass_color  # type: int
        self.cap_color = cap_color      # type: int
        self.cap_color_reliability = cap_color_reliability  # type: str
        self.respirator_color_reliability = respirator_color_reliability  # type: str
        self.ethic_code_reliability = ethic_code_reliability  # type: str
        self.gender_code_reliability = gender_code_reliability  # type: str
        self.glass_color_reliability = glass_color_reliability  # type: str
        self.skin_color_reliability = skin_color_reliability  # type: str
        self.mustache_style_reliability = mustache_style_reliability  # type: str
        self.cap_style_reliability = cap_style_reliability  # type: str
        self.face_style_reliability = face_style_reliability  # type: str
        self.glass_style_reliability = glass_style_reliability  # type: str
        self.age_up_limit_reliability = age_up_limit_reliability  # type: str
        self.hair_style_reliability = hair_style_reliability  # type: str
        self.age_lower_limit_reliability = age_lower_limit_reliability  # type: str
        self.hair_color_reliability = hair_color_reliability  # type: str
        self.feature_data = feature_data  # type: List[float]

    def validate(self):
        self.validate_required(self.mustache_style, 'mustache_style')
        self.validate_required(self.face_style, 'face_style')
        self.validate_required(self.cap_style, 'cap_style')
        self.validate_required(self.skin_color, 'skin_color')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.hair_style, 'hair_style')
        self.validate_required(self.gender_code, 'gender_code')
        self.validate_required(self.respirator_color, 'respirator_color')
        self.validate_required(self.ethic_code, 'ethic_code')
        self.validate_required(self.age_lower_limit, 'age_lower_limit')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.hair_color, 'hair_color')
        self.validate_required(self.age_up_limit, 'age_up_limit')
        self.validate_required(self.glass_style, 'glass_style')
        self.validate_required(self.glass_color, 'glass_color')
        self.validate_required(self.cap_color, 'cap_color')
        self.validate_required(self.cap_color_reliability, 'cap_color_reliability')
        self.validate_required(self.respirator_color_reliability, 'respirator_color_reliability')
        self.validate_required(self.ethic_code_reliability, 'ethic_code_reliability')
        self.validate_required(self.gender_code_reliability, 'gender_code_reliability')
        self.validate_required(self.glass_color_reliability, 'glass_color_reliability')
        self.validate_required(self.skin_color_reliability, 'skin_color_reliability')
        self.validate_required(self.mustache_style_reliability, 'mustache_style_reliability')
        self.validate_required(self.cap_style_reliability, 'cap_style_reliability')
        self.validate_required(self.face_style_reliability, 'face_style_reliability')
        self.validate_required(self.glass_style_reliability, 'glass_style_reliability')
        self.validate_required(self.age_up_limit_reliability, 'age_up_limit_reliability')
        self.validate_required(self.hair_style_reliability, 'hair_style_reliability')
        self.validate_required(self.age_lower_limit_reliability, 'age_lower_limit_reliability')
        self.validate_required(self.hair_color_reliability, 'hair_color_reliability')
        self.validate_required(self.feature_data, 'feature_data')

    def to_map(self):
        result = {}
        result['MustacheStyle'] = self.mustache_style
        result['FaceStyle'] = self.face_style
        result['CapStyle'] = self.cap_style
        result['SkinColor'] = self.skin_color
        result['RightBottomY'] = self.right_bottom_y
        result['RightBottomX'] = self.right_bottom_x
        result['HairStyle'] = self.hair_style
        result['GenderCode'] = self.gender_code
        result['RespiratorColor'] = self.respirator_color
        result['EthicCode'] = self.ethic_code
        result['AgeLowerLimit'] = self.age_lower_limit
        result['LeftTopY'] = self.left_top_y
        result['LeftTopX'] = self.left_top_x
        result['HairColor'] = self.hair_color
        result['AgeUpLimit'] = self.age_up_limit
        result['GlassStyle'] = self.glass_style
        result['GlassColor'] = self.glass_color
        result['CapColor'] = self.cap_color
        result['CapColorReliability'] = self.cap_color_reliability
        result['RespiratorColorReliability'] = self.respirator_color_reliability
        result['EthicCodeReliability'] = self.ethic_code_reliability
        result['GenderCodeReliability'] = self.gender_code_reliability
        result['GlassColorReliability'] = self.glass_color_reliability
        result['SkinColorReliability'] = self.skin_color_reliability
        result['MustacheStyleReliability'] = self.mustache_style_reliability
        result['CapStyleReliability'] = self.cap_style_reliability
        result['FaceStyleReliability'] = self.face_style_reliability
        result['GlassStyleReliability'] = self.glass_style_reliability
        result['AgeUpLimitReliability'] = self.age_up_limit_reliability
        result['HairStyleReliability'] = self.hair_style_reliability
        result['AgeLowerLimitReliability'] = self.age_lower_limit_reliability
        result['HairColorReliability'] = self.hair_color_reliability
        result['FeatureData'] = self.feature_data
        return result

    def from_map(self, map={}):
        self.mustache_style = map.get('MustacheStyle')
        self.face_style = map.get('FaceStyle')
        self.cap_style = map.get('CapStyle')
        self.skin_color = map.get('SkinColor')
        self.right_bottom_y = map.get('RightBottomY')
        self.right_bottom_x = map.get('RightBottomX')
        self.hair_style = map.get('HairStyle')
        self.gender_code = map.get('GenderCode')
        self.respirator_color = map.get('RespiratorColor')
        self.ethic_code = map.get('EthicCode')
        self.age_lower_limit = map.get('AgeLowerLimit')
        self.left_top_y = map.get('LeftTopY')
        self.left_top_x = map.get('LeftTopX')
        self.hair_color = map.get('HairColor')
        self.age_up_limit = map.get('AgeUpLimit')
        self.glass_style = map.get('GlassStyle')
        self.glass_color = map.get('GlassColor')
        self.cap_color = map.get('CapColor')
        self.cap_color_reliability = map.get('CapColorReliability')
        self.respirator_color_reliability = map.get('RespiratorColorReliability')
        self.ethic_code_reliability = map.get('EthicCodeReliability')
        self.gender_code_reliability = map.get('GenderCodeReliability')
        self.glass_color_reliability = map.get('GlassColorReliability')
        self.skin_color_reliability = map.get('SkinColorReliability')
        self.mustache_style_reliability = map.get('MustacheStyleReliability')
        self.cap_style_reliability = map.get('CapStyleReliability')
        self.face_style_reliability = map.get('FaceStyleReliability')
        self.glass_style_reliability = map.get('GlassStyleReliability')
        self.age_up_limit_reliability = map.get('AgeUpLimitReliability')
        self.hair_style_reliability = map.get('HairStyleReliability')
        self.age_lower_limit_reliability = map.get('AgeLowerLimitReliability')
        self.hair_color_reliability = map.get('HairColorReliability')
        self.feature_data = map.get('FeatureData')
        return self


class GetFaceModelResultResponseData(TeaModel):
    def __init__(self, records=None):
        self.records = records          # type: List[GetFaceModelResultResponseDataRecords]

    def validate(self):
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = GetFaceModelResultResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class CreateCorpGroupRequest(TeaModel):
    def __init__(self, corp_id=None, group_id=None, client_token=None):
        self.corp_id = corp_id          # type: str
        self.group_id = group_id        # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.group_id, 'group_id')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GroupId'] = self.group_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.group_id = map.get('GroupId')
        self.client_token = map.get('ClientToken')
        return self


class CreateCorpGroupResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class ListCorpGroupsRequest(TeaModel):
    def __init__(self, corp_id=None, page_number=None, page_size=None):
        self.corp_id = corp_id          # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListCorpGroupsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListCorpGroupsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListCorpGroupsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListCorpGroupsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[str]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = self.records
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = map.get('Records')
        return self


class DeleteCorpGroupRequest(TeaModel):
    def __init__(self, corp_id=None, group_id=None):
        self.corp_id = corp_id          # type: str
        self.group_id = group_id        # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.group_id, 'group_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GroupId'] = self.group_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.group_id = map.get('GroupId')
        return self


class DeleteCorpGroupResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        return self


class InvokeMotorModelRequest(TeaModel):
    def __init__(self, pic_id=None, corp_id=None, pic_path=None, pic_url=None):
        self.pic_id = pic_id            # type: str
        self.corp_id = corp_id          # type: str
        self.pic_path = pic_path        # type: str
        self.pic_url = pic_url          # type: str

    def validate(self):
        self.validate_required(self.pic_id, 'pic_id')
        self.validate_required(self.corp_id, 'corp_id')

    def to_map(self):
        result = {}
        result['PicId'] = self.pic_id
        result['CorpId'] = self.corp_id
        result['PicPath'] = self.pic_path
        result['PicUrl'] = self.pic_url
        return result

    def from_map(self, map={}):
        self.pic_id = map.get('PicId')
        self.corp_id = map.get('CorpId')
        self.pic_path = map.get('PicPath')
        self.pic_url = map.get('PicUrl')
        return self


class InvokeMotorModelResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: InvokeMotorModelResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = InvokeMotorModelResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class InvokeMotorModelResponseData(TeaModel):
    def __init__(self, struct_list=None):
        self.struct_list = struct_list  # type: str

    def validate(self):
        self.validate_required(self.struct_list, 'struct_list')

    def to_map(self):
        result = {}
        result['StructList'] = self.struct_list
        return result

    def from_map(self, map={}):
        self.struct_list = map.get('StructList')
        return self


class GetDeviceConfigRequest(TeaModel):
    def __init__(self, device_sn=None, device_time_stamp=None):
        self.device_sn = device_sn      # type: str
        self.device_time_stamp = device_time_stamp  # type: str

    def validate(self):
        self.validate_required(self.device_sn, 'device_sn')
        self.validate_required(self.device_time_stamp, 'device_time_stamp')

    def to_map(self):
        result = {}
        result['DeviceSn'] = self.device_sn
        result['DeviceTimeStamp'] = self.device_time_stamp
        return result

    def from_map(self, map={}):
        self.device_sn = map.get('DeviceSn')
        self.device_time_stamp = map.get('DeviceTimeStamp')
        return self


class GetDeviceConfigResponse(TeaModel):
    def __init__(self, audio_enable=None, audio_format=None, bit_rate=None, code=None, device_address=None,
                 device_name=None, encode_format=None, frame_rate=None, gov_length=None, latitude=None, longitude=None,
                 message=None, osdtime_enable=None, osdtime_type=None, osdtime_x=None, osdtime_y=None, request_id=None,
                 resolution=None, retry_interval=None, device_id=None, user_name=None, pass_word=None, protocol=None,
                 server_id=None, server_port=None, server_ip=None, osdlist=None):
        self.audio_enable = audio_enable  # type: bool
        self.audio_format = audio_format  # type: str
        self.bit_rate = bit_rate        # type: str
        self.code = code                # type: str
        self.device_address = device_address  # type: str
        self.device_name = device_name  # type: str
        self.encode_format = encode_format  # type: str
        self.frame_rate = frame_rate    # type: str
        self.gov_length = gov_length    # type: int
        self.latitude = latitude        # type: str
        self.longitude = longitude      # type: str
        self.message = message          # type: str
        self.osdtime_enable = osdtime_enable  # type: str
        self.osdtime_type = osdtime_type  # type: str
        self.osdtime_x = osdtime_x      # type: str
        self.osdtime_y = osdtime_y      # type: str
        self.request_id = request_id    # type: str
        self.resolution = resolution    # type: str
        self.retry_interval = retry_interval  # type: str
        self.device_id = device_id      # type: str
        self.user_name = user_name      # type: str
        self.pass_word = pass_word      # type: str
        self.protocol = protocol        # type: str
        self.server_id = server_id      # type: str
        self.server_port = server_port  # type: str
        self.server_ip = server_ip      # type: str
        self.osdlist = osdlist          # type: List[GetDeviceConfigResponseOSDList]

    def validate(self):
        self.validate_required(self.audio_enable, 'audio_enable')
        self.validate_required(self.audio_format, 'audio_format')
        self.validate_required(self.bit_rate, 'bit_rate')
        self.validate_required(self.code, 'code')
        self.validate_required(self.device_address, 'device_address')
        self.validate_required(self.device_name, 'device_name')
        self.validate_required(self.encode_format, 'encode_format')
        self.validate_required(self.frame_rate, 'frame_rate')
        self.validate_required(self.gov_length, 'gov_length')
        self.validate_required(self.latitude, 'latitude')
        self.validate_required(self.longitude, 'longitude')
        self.validate_required(self.message, 'message')
        self.validate_required(self.osdtime_enable, 'osdtime_enable')
        self.validate_required(self.osdtime_type, 'osdtime_type')
        self.validate_required(self.osdtime_x, 'osdtime_x')
        self.validate_required(self.osdtime_y, 'osdtime_y')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.retry_interval, 'retry_interval')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.pass_word, 'pass_word')
        self.validate_required(self.protocol, 'protocol')
        self.validate_required(self.server_id, 'server_id')
        self.validate_required(self.server_port, 'server_port')
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.osdlist, 'osdlist')
        if self.osdlist:
            for k in self.osdlist:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AudioEnable'] = self.audio_enable
        result['AudioFormat'] = self.audio_format
        result['BitRate'] = self.bit_rate
        result['Code'] = self.code
        result['DeviceAddress'] = self.device_address
        result['DeviceName'] = self.device_name
        result['EncodeFormat'] = self.encode_format
        result['FrameRate'] = self.frame_rate
        result['GovLength'] = self.gov_length
        result['Latitude'] = self.latitude
        result['Longitude'] = self.longitude
        result['Message'] = self.message
        result['OSDTimeEnable'] = self.osdtime_enable
        result['OSDTimeType'] = self.osdtime_type
        result['OSDTimeX'] = self.osdtime_x
        result['OSDTimeY'] = self.osdtime_y
        result['RequestId'] = self.request_id
        result['Resolution'] = self.resolution
        result['RetryInterval'] = self.retry_interval
        result['DeviceId'] = self.device_id
        result['UserName'] = self.user_name
        result['PassWord'] = self.pass_word
        result['Protocol'] = self.protocol
        result['ServerId'] = self.server_id
        result['ServerPort'] = self.server_port
        result['ServerIp'] = self.server_ip
        result['OSDList'] = []
        if self.osdlist is not None:
            for k in self.osdlist:
                result['OSDList'].append(k.to_map() if k else None)
        else:
            result['OSDList'] = None
        return result

    def from_map(self, map={}):
        self.audio_enable = map.get('AudioEnable')
        self.audio_format = map.get('AudioFormat')
        self.bit_rate = map.get('BitRate')
        self.code = map.get('Code')
        self.device_address = map.get('DeviceAddress')
        self.device_name = map.get('DeviceName')
        self.encode_format = map.get('EncodeFormat')
        self.frame_rate = map.get('FrameRate')
        self.gov_length = map.get('GovLength')
        self.latitude = map.get('Latitude')
        self.longitude = map.get('Longitude')
        self.message = map.get('Message')
        self.osdtime_enable = map.get('OSDTimeEnable')
        self.osdtime_type = map.get('OSDTimeType')
        self.osdtime_x = map.get('OSDTimeX')
        self.osdtime_y = map.get('OSDTimeY')
        self.request_id = map.get('RequestId')
        self.resolution = map.get('Resolution')
        self.retry_interval = map.get('RetryInterval')
        self.device_id = map.get('DeviceId')
        self.user_name = map.get('UserName')
        self.pass_word = map.get('PassWord')
        self.protocol = map.get('Protocol')
        self.server_id = map.get('ServerId')
        self.server_port = map.get('ServerPort')
        self.server_ip = map.get('ServerIp')
        self.osdlist = []
        if map.get('OSDList') is not None:
            for k in map.get('OSDList'):
                temp_model = GetDeviceConfigResponseOSDList()
                self.osdlist.append(temp_model.from_map(k))
        else:
            self.osdlist = None
        return self


class GetDeviceConfigResponseOSDList(TeaModel):
    def __init__(self, text=None, left_top_x=None, left_top_y=None):
        self.text = text                # type: str
        self.left_top_x = left_top_x    # type: str
        self.left_top_y = left_top_y    # type: str

    def validate(self):
        self.validate_required(self.text, 'text')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')

    def to_map(self):
        result = {}
        result['Text'] = self.text
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        return result

    def from_map(self, map={}):
        self.text = map.get('Text')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        return self


class SyncDeviceTimeRequest(TeaModel):
    def __init__(self, device_sn=None, device_time_stamp=None):
        self.device_sn = device_sn      # type: str
        self.device_time_stamp = device_time_stamp  # type: str

    def validate(self):
        self.validate_required(self.device_sn, 'device_sn')
        self.validate_required(self.device_time_stamp, 'device_time_stamp')

    def to_map(self):
        result = {}
        result['DeviceSn'] = self.device_sn
        result['DeviceTimeStamp'] = self.device_time_stamp
        return result

    def from_map(self, map={}):
        self.device_sn = map.get('DeviceSn')
        self.device_time_stamp = map.get('DeviceTimeStamp')
        return self


class SyncDeviceTimeResponse(TeaModel):
    def __init__(self, code=None, message=None, ntpserver=None, request_id=None, retry_interval=None,
                 sync_interval=None, time_stamp=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.ntpserver = ntpserver      # type: str
        self.request_id = request_id    # type: str
        self.retry_interval = retry_interval  # type: str
        self.sync_interval = sync_interval  # type: str
        self.time_stamp = time_stamp    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.ntpserver, 'ntpserver')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.retry_interval, 'retry_interval')
        self.validate_required(self.sync_interval, 'sync_interval')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['NTPServer'] = self.ntpserver
        result['RequestId'] = self.request_id
        result['RetryInterval'] = self.retry_interval
        result['SyncInterval'] = self.sync_interval
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.ntpserver = map.get('NTPServer')
        self.request_id = map.get('RequestId')
        self.retry_interval = map.get('RetryInterval')
        self.sync_interval = map.get('SyncInterval')
        self.time_stamp = map.get('TimeStamp')
        return self


class RegisterDeviceRequest(TeaModel):
    def __init__(self, device_sn=None, device_id=None, server_id=None, device_time_stamp=None):
        self.device_sn = device_sn      # type: str
        self.device_id = device_id      # type: str
        self.server_id = server_id      # type: str
        self.device_time_stamp = device_time_stamp  # type: str

    def validate(self):
        self.validate_required(self.device_sn, 'device_sn')
        self.validate_required(self.device_time_stamp, 'device_time_stamp')

    def to_map(self):
        result = {}
        result['DeviceSn'] = self.device_sn
        result['DeviceId'] = self.device_id
        result['ServerId'] = self.server_id
        result['DeviceTimeStamp'] = self.device_time_stamp
        return result

    def from_map(self, map={}):
        self.device_sn = map.get('DeviceSn')
        self.device_id = map.get('DeviceId')
        self.server_id = map.get('ServerId')
        self.device_time_stamp = map.get('DeviceTimeStamp')
        return self


class RegisterDeviceResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, retry_interval=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.retry_interval = retry_interval  # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.retry_interval, 'retry_interval')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['RetryInterval'] = self.retry_interval
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.retry_interval = map.get('RetryInterval')
        return self


class ReportDeviceCapacityRequest(TeaModel):
    def __init__(self, longitude=None, latitude=None, audio_format=None, preset_num=None, ptzcapacity=None,
                 device_sn=None, stream_capacities=None, device_time_stamp=None):
        self.longitude = longitude      # type: str
        self.latitude = latitude        # type: str
        self.audio_format = audio_format  # type: str
        self.preset_num = preset_num    # type: str
        self.ptzcapacity = ptzcapacity  # type: str
        self.device_sn = device_sn      # type: str
        self.stream_capacities = stream_capacities  # type: List[ReportDeviceCapacityRequestStreamCapacities]
        self.device_time_stamp = device_time_stamp  # type: str

    def validate(self):
        self.validate_required(self.device_sn, 'device_sn')
        self.validate_required(self.stream_capacities, 'stream_capacities')
        if self.stream_capacities:
            for k in self.stream_capacities:
                if k:
                    k.validate()
        self.validate_required(self.device_time_stamp, 'device_time_stamp')

    def to_map(self):
        result = {}
        result['Longitude'] = self.longitude
        result['Latitude'] = self.latitude
        result['AudioFormat'] = self.audio_format
        result['PresetNum'] = self.preset_num
        result['PTZCapacity'] = self.ptzcapacity
        result['DeviceSn'] = self.device_sn
        result['StreamCapacities'] = []
        if self.stream_capacities is not None:
            for k in self.stream_capacities:
                result['StreamCapacities'].append(k.to_map() if k else None)
        else:
            result['StreamCapacities'] = None
        result['DeviceTimeStamp'] = self.device_time_stamp
        return result

    def from_map(self, map={}):
        self.longitude = map.get('Longitude')
        self.latitude = map.get('Latitude')
        self.audio_format = map.get('AudioFormat')
        self.preset_num = map.get('PresetNum')
        self.ptzcapacity = map.get('PTZCapacity')
        self.device_sn = map.get('DeviceSn')
        self.stream_capacities = []
        if map.get('StreamCapacities') is not None:
            for k in map.get('StreamCapacities'):
                temp_model = ReportDeviceCapacityRequestStreamCapacities()
                self.stream_capacities.append(temp_model.from_map(k))
        else:
            self.stream_capacities = None
        self.device_time_stamp = map.get('DeviceTimeStamp')
        return self


class ReportDeviceCapacityRequestStreamCapacities(TeaModel):
    def __init__(self, encode_format=None, resolution=None, max_frame_rate=None, max_stream=None,
                 bitrate_range=None, gov_length_range=None):
        self.encode_format = encode_format  # type: str
        self.resolution = resolution    # type: str
        self.max_frame_rate = max_frame_rate  # type: str
        self.max_stream = max_stream    # type: str
        self.bitrate_range = bitrate_range  # type: str
        self.gov_length_range = gov_length_range  # type: str

    def validate(self):
        self.validate_required(self.encode_format, 'encode_format')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.max_frame_rate, 'max_frame_rate')
        self.validate_required(self.max_stream, 'max_stream')
        self.validate_required(self.bitrate_range, 'bitrate_range')
        self.validate_required(self.gov_length_range, 'gov_length_range')

    def to_map(self):
        result = {}
        result['EncodeFormat'] = self.encode_format
        result['Resolution'] = self.resolution
        result['MaxFrameRate'] = self.max_frame_rate
        result['MaxStream'] = self.max_stream
        result['BitrateRange'] = self.bitrate_range
        result['GovLengthRange'] = self.gov_length_range
        return result

    def from_map(self, map={}):
        self.encode_format = map.get('EncodeFormat')
        self.resolution = map.get('Resolution')
        self.max_frame_rate = map.get('MaxFrameRate')
        self.max_stream = map.get('MaxStream')
        self.bitrate_range = map.get('BitrateRange')
        self.gov_length_range = map.get('GovLengthRange')
        return self


class ReportDeviceCapacityResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, retry_interval=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.retry_interval = retry_interval  # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.retry_interval, 'retry_interval')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['RetryInterval'] = self.retry_interval
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.retry_interval = map.get('RetryInterval')
        return self


class SaveVideoSummaryTaskVideoRequest(TeaModel):
    def __init__(self, corp_id=None, task_id=None, save_video=None):
        self.corp_id = corp_id          # type: str
        self.task_id = task_id          # type: int
        self.save_video = save_video    # type: bool

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.save_video, 'save_video')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TaskId'] = self.task_id
        result['SaveVideo'] = self.save_video
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.task_id = map.get('TaskId')
        self.save_video = map.get('SaveVideo')
        return self


class SaveVideoSummaryTaskVideoResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class ListBodyAlgorithmResultsRequest(TeaModel):
    def __init__(self, corp_id=None, algorithm_type=None, data_source_id=None, start_time=None, end_time=None,
                 page_number=None, page_size=None, cap_style=None):
        self.corp_id = corp_id          # type: str
        self.algorithm_type = algorithm_type  # type: str
        self.data_source_id = data_source_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.cap_style = cap_style      # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.algorithm_type, 'algorithm_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['AlgorithmType'] = self.algorithm_type
        result['DataSourceId'] = self.data_source_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['CapStyle'] = self.cap_style
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.algorithm_type = map.get('AlgorithmType')
        self.data_source_id = map.get('DataSourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.cap_style = map.get('CapStyle')
        return self


class ListBodyAlgorithmResultsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListBodyAlgorithmResultsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListBodyAlgorithmResultsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListBodyAlgorithmResultsResponseDataRecords(TeaModel):
    def __init__(self, cap_style=None, corp_id=None, data_source_id=None, person_id=None, gender_code=None,
                 hair_style=None, left_top_x=None, left_top_y=None, max_age=None, min_age=None, pic_url_path=None,
                 right_bottom_x=None, right_bottom_y=None, shot_time=None, target_pic_url_path=None, coat_length=None,
                 coat_style=None, trousers_length=None, trousers_style=None, coat_color=None, trousers_color=None,
                 source_id=None):
        self.cap_style = cap_style      # type: str
        self.corp_id = corp_id          # type: str
        self.data_source_id = data_source_id  # type: str
        self.person_id = person_id      # type: str
        self.gender_code = gender_code  # type: str
        self.hair_style = hair_style    # type: str
        self.left_top_x = left_top_x    # type: float
        self.left_top_y = left_top_y    # type: float
        self.max_age = max_age          # type: str
        self.min_age = min_age          # type: str
        self.pic_url_path = pic_url_path  # type: str
        self.right_bottom_x = right_bottom_x  # type: float
        self.right_bottom_y = right_bottom_y  # type: float
        self.shot_time = shot_time      # type: str
        self.target_pic_url_path = target_pic_url_path  # type: str
        self.coat_length = coat_length  # type: str
        self.coat_style = coat_style    # type: str
        self.trousers_length = trousers_length  # type: str
        self.trousers_style = trousers_style  # type: str
        self.coat_color = coat_color    # type: str
        self.trousers_color = trousers_color  # type: str
        self.source_id = source_id      # type: str

    def validate(self):
        self.validate_required(self.cap_style, 'cap_style')
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.data_source_id, 'data_source_id')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.gender_code, 'gender_code')
        self.validate_required(self.hair_style, 'hair_style')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.max_age, 'max_age')
        self.validate_required(self.min_age, 'min_age')
        self.validate_required(self.pic_url_path, 'pic_url_path')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.target_pic_url_path, 'target_pic_url_path')
        self.validate_required(self.coat_length, 'coat_length')
        self.validate_required(self.coat_style, 'coat_style')
        self.validate_required(self.trousers_length, 'trousers_length')
        self.validate_required(self.trousers_style, 'trousers_style')
        self.validate_required(self.coat_color, 'coat_color')
        self.validate_required(self.trousers_color, 'trousers_color')
        self.validate_required(self.source_id, 'source_id')

    def to_map(self):
        result = {}
        result['CapStyle'] = self.cap_style
        result['CorpId'] = self.corp_id
        result['DataSourceId'] = self.data_source_id
        result['PersonId'] = self.person_id
        result['GenderCode'] = self.gender_code
        result['HairStyle'] = self.hair_style
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['MaxAge'] = self.max_age
        result['MinAge'] = self.min_age
        result['PicUrlPath'] = self.pic_url_path
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['ShotTime'] = self.shot_time
        result['TargetPicUrlPath'] = self.target_pic_url_path
        result['CoatLength'] = self.coat_length
        result['CoatStyle'] = self.coat_style
        result['TrousersLength'] = self.trousers_length
        result['TrousersStyle'] = self.trousers_style
        result['CoatColor'] = self.coat_color
        result['TrousersColor'] = self.trousers_color
        result['SourceId'] = self.source_id
        return result

    def from_map(self, map={}):
        self.cap_style = map.get('CapStyle')
        self.corp_id = map.get('CorpId')
        self.data_source_id = map.get('DataSourceId')
        self.person_id = map.get('PersonId')
        self.gender_code = map.get('GenderCode')
        self.hair_style = map.get('HairStyle')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.max_age = map.get('MaxAge')
        self.min_age = map.get('MinAge')
        self.pic_url_path = map.get('PicUrlPath')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.shot_time = map.get('ShotTime')
        self.target_pic_url_path = map.get('TargetPicUrlPath')
        self.coat_length = map.get('CoatLength')
        self.coat_style = map.get('CoatStyle')
        self.trousers_length = map.get('TrousersLength')
        self.trousers_style = map.get('TrousersStyle')
        self.coat_color = map.get('CoatColor')
        self.trousers_color = map.get('TrousersColor')
        self.source_id = map.get('SourceId')
        return self


class ListBodyAlgorithmResultsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[ListBodyAlgorithmResultsResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListBodyAlgorithmResultsResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class AddDataSourceRequest(TeaModel):
    def __init__(self, corp_id=None, data_source_name=None, data_source_type=None, description=None,
                 file_retention_days=None):
        self.corp_id = corp_id          # type: str
        self.data_source_name = data_source_name  # type: str
        self.data_source_type = data_source_type  # type: str
        self.description = description  # type: str
        self.file_retention_days = file_retention_days  # type: int

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.data_source_name, 'data_source_name')
        self.validate_required(self.data_source_type, 'data_source_type')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['DataSourceName'] = self.data_source_name
        result['DataSourceType'] = self.data_source_type
        result['Description'] = self.description
        result['FileRetentionDays'] = self.file_retention_days
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.data_source_name = map.get('DataSourceName')
        self.data_source_type = map.get('DataSourceType')
        self.description = map.get('Description')
        self.file_retention_days = map.get('FileRetentionDays')
        return self


class AddDataSourceResponse(TeaModel):
    def __init__(self, code=None, message=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: AddDataSourceResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = AddDataSourceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AddDataSourceResponseData(TeaModel):
    def __init__(self, data_source_id=None, kafka_topic=None, oss_path=None):
        self.data_source_id = data_source_id  # type: str
        self.kafka_topic = kafka_topic  # type: str
        self.oss_path = oss_path        # type: str

    def validate(self):
        self.validate_required(self.data_source_id, 'data_source_id')
        self.validate_required(self.kafka_topic, 'kafka_topic')
        self.validate_required(self.oss_path, 'oss_path')

    def to_map(self):
        result = {}
        result['DataSourceId'] = self.data_source_id
        result['KafkaTopic'] = self.kafka_topic
        result['OssPath'] = self.oss_path
        return result

    def from_map(self, map={}):
        self.data_source_id = map.get('DataSourceId')
        self.kafka_topic = map.get('KafkaTopic')
        self.oss_path = map.get('OssPath')
        return self


class GetVideoComposeResultRequest(TeaModel):
    def __init__(self, corp_id=None, task_request_id=None):
        self.corp_id = corp_id          # type: str
        self.task_request_id = task_request_id  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.task_request_id, 'task_request_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TaskRequestId'] = self.task_request_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.task_request_id = map.get('TaskRequestId')
        return self


class GetVideoComposeResultResponse(TeaModel):
    def __init__(self, message=None, request_id=None, video_url=None, code=None, status=None):
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.video_url = video_url      # type: str
        self.code = code                # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.code, 'code')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['VideoUrl'] = self.video_url
        result['Code'] = self.code
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.video_url = map.get('VideoUrl')
        self.code = map.get('Code')
        self.status = map.get('Status')
        return self


class CreateVideoComposeTaskRequest(TeaModel):
    def __init__(self, corp_id=None, bucket_name=None, domain_name=None, image_file_names=None,
                 audio_file_name=None, image_parameters=None, video_format=None, video_frame_rate=None):
        self.corp_id = corp_id          # type: str
        self.bucket_name = bucket_name  # type: str
        self.domain_name = domain_name  # type: str
        self.image_file_names = image_file_names  # type: str
        self.audio_file_name = audio_file_name  # type: str
        self.image_parameters = image_parameters  # type: str
        self.video_format = video_format  # type: str
        self.video_frame_rate = video_frame_rate  # type: int

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.bucket_name, 'bucket_name')
        self.validate_required(self.image_file_names, 'image_file_names')
        self.validate_required(self.audio_file_name, 'audio_file_name')
        self.validate_required(self.image_parameters, 'image_parameters')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['BucketName'] = self.bucket_name
        result['DomainName'] = self.domain_name
        result['ImageFileNames'] = self.image_file_names
        result['AudioFileName'] = self.audio_file_name
        result['ImageParameters'] = self.image_parameters
        result['VideoFormat'] = self.video_format
        result['VideoFrameRate'] = self.video_frame_rate
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.bucket_name = map.get('BucketName')
        self.domain_name = map.get('DomainName')
        self.image_file_names = map.get('ImageFileNames')
        self.audio_file_name = map.get('AudioFileName')
        self.image_parameters = map.get('ImageParameters')
        self.video_format = map.get('VideoFormat')
        self.video_frame_rate = map.get('VideoFrameRate')
        return self


class CreateVideoComposeTaskResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, domain_name=None, bucket_name=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.bucket_name = bucket_name  # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.bucket_name, 'bucket_name')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['BucketName'] = self.bucket_name
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.bucket_name = map.get('BucketName')
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(self, corp_id=None, data_source_id=None):
        self.corp_id = corp_id          # type: str
        self.data_source_id = data_source_id  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.data_source_id, 'data_source_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['DataSourceId'] = self.data_source_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.data_source_id = map.get('DataSourceId')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        return self


class UploadFileRequest(TeaModel):
    def __init__(self, file_type=None, md5=None, corp_id=None, file_content=None, file_name=None,
                 file_alias_name=None, data_source_id=None, file_path=None):
        self.file_type = file_type      # type: str
        self.md5 = md5                  # type: str
        self.corp_id = corp_id          # type: str
        self.file_content = file_content  # type: str
        self.file_name = file_name      # type: str
        self.file_alias_name = file_alias_name  # type: str
        self.data_source_id = data_source_id  # type: str
        self.file_path = file_path      # type: str

    def validate(self):
        self.validate_required(self.file_type, 'file_type')
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.data_source_id, 'data_source_id')

    def to_map(self):
        result = {}
        result['FileType'] = self.file_type
        result['MD5'] = self.md5
        result['CorpId'] = self.corp_id
        result['FileContent'] = self.file_content
        result['FileName'] = self.file_name
        result['FileAliasName'] = self.file_alias_name
        result['DataSourceId'] = self.data_source_id
        result['FilePath'] = self.file_path
        return result

    def from_map(self, map={}):
        self.file_type = map.get('FileType')
        self.md5 = map.get('MD5')
        self.corp_id = map.get('CorpId')
        self.file_content = map.get('FileContent')
        self.file_name = map.get('FileName')
        self.file_alias_name = map.get('FileAliasName')
        self.data_source_id = map.get('DataSourceId')
        self.file_path = map.get('FilePath')
        return self


class UploadFileResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: UploadFileResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = UploadFileResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class UploadFileResponseDataRecords(TeaModel):
    def __init__(self, oss_path=None, source_id=None):
        self.oss_path = oss_path        # type: str
        self.source_id = source_id      # type: str

    def validate(self):
        self.validate_required(self.oss_path, 'oss_path')
        self.validate_required(self.source_id, 'source_id')

    def to_map(self):
        result = {}
        result['OssPath'] = self.oss_path
        result['SourceId'] = self.source_id
        return result

    def from_map(self, map={}):
        self.oss_path = map.get('OssPath')
        self.source_id = map.get('SourceId')
        return self


class UploadFileResponseData(TeaModel):
    def __init__(self, records=None):
        self.records = records          # type: List[UploadFileResponseDataRecords]

    def validate(self):
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = UploadFileResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class ListEventAlgorithmResultsRequest(TeaModel):
    def __init__(self, corp_id=None, event_type=None, data_source_id=None, start_time=None, end_time=None,
                 page_number=None, page_size=None, extend_value=None):
        self.corp_id = corp_id          # type: str
        self.event_type = event_type    # type: str
        self.data_source_id = data_source_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.extend_value = extend_value  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['EventType'] = self.event_type
        result['DataSourceId'] = self.data_source_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ExtendValue'] = self.extend_value
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.event_type = map.get('EventType')
        self.data_source_id = map.get('DataSourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.extend_value = map.get('ExtendValue')
        return self


class ListEventAlgorithmResultsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, extend_value=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.extend_value = extend_value  # type: str
        self.data = data                # type: ListEventAlgorithmResultsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.extend_value, 'extend_value')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['ExtendValue'] = self.extend_value
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.extend_value = map.get('ExtendValue')
        if map.get('Data') is not None:
            temp_model = ListEventAlgorithmResultsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListEventAlgorithmResultsResponseDataRecords(TeaModel):
    def __init__(self, cap_style=None, corp_id=None, data_source_id=None, event_type=None, face_count=None,
                 pic_url_path=None, shot_time=None, target_pic_url_path=None, record_id=None, extend_value=None,
                 extend_value_two=None, extend_value_three=None):
        self.cap_style = cap_style      # type: str
        self.corp_id = corp_id          # type: str
        self.data_source_id = data_source_id  # type: str
        self.event_type = event_type    # type: str
        self.face_count = face_count    # type: str
        self.pic_url_path = pic_url_path  # type: str
        self.shot_time = shot_time      # type: str
        self.target_pic_url_path = target_pic_url_path  # type: str
        self.record_id = record_id      # type: str
        self.extend_value = extend_value  # type: str
        self.extend_value_two = extend_value_two  # type: str
        self.extend_value_three = extend_value_three  # type: str

    def validate(self):
        self.validate_required(self.cap_style, 'cap_style')
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.data_source_id, 'data_source_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.face_count, 'face_count')
        self.validate_required(self.pic_url_path, 'pic_url_path')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.target_pic_url_path, 'target_pic_url_path')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.extend_value, 'extend_value')
        self.validate_required(self.extend_value_two, 'extend_value_two')
        self.validate_required(self.extend_value_three, 'extend_value_three')

    def to_map(self):
        result = {}
        result['CapStyle'] = self.cap_style
        result['CorpId'] = self.corp_id
        result['DataSourceId'] = self.data_source_id
        result['EventType'] = self.event_type
        result['FaceCount'] = self.face_count
        result['PicUrlPath'] = self.pic_url_path
        result['ShotTime'] = self.shot_time
        result['TargetPicUrlPath'] = self.target_pic_url_path
        result['RecordId'] = self.record_id
        result['ExtendValue'] = self.extend_value
        result['ExtendValueTwo'] = self.extend_value_two
        result['ExtendValueThree'] = self.extend_value_three
        return result

    def from_map(self, map={}):
        self.cap_style = map.get('CapStyle')
        self.corp_id = map.get('CorpId')
        self.data_source_id = map.get('DataSourceId')
        self.event_type = map.get('EventType')
        self.face_count = map.get('FaceCount')
        self.pic_url_path = map.get('PicUrlPath')
        self.shot_time = map.get('ShotTime')
        self.target_pic_url_path = map.get('TargetPicUrlPath')
        self.record_id = map.get('RecordId')
        self.extend_value = map.get('ExtendValue')
        self.extend_value_two = map.get('ExtendValueTwo')
        self.extend_value_three = map.get('ExtendValueThree')
        return self


class ListEventAlgorithmResultsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[ListEventAlgorithmResultsResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListEventAlgorithmResultsResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class DeleteVideoSummaryTaskRequest(TeaModel):
    def __init__(self, corp_id=None, task_id=None):
        self.corp_id = corp_id          # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.task_id = map.get('TaskId')
        return self


class DeleteVideoSummaryTaskResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class GetVideoSummaryTaskResultRequest(TeaModel):
    def __init__(self, corp_id=None, task_id=None):
        self.corp_id = corp_id          # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.task_id = map.get('TaskId')
        return self


class GetVideoSummaryTaskResultResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class CreateVideoSummaryTaskRequest(TeaModel):
    def __init__(self, corp_id=None, device_id=None, start_time_stamp=None, end_time_stamp=None, option_list=None,
                 live_video_summary=None):
        self.corp_id = corp_id          # type: str
        self.device_id = device_id      # type: str
        self.start_time_stamp = start_time_stamp  # type: int
        self.end_time_stamp = end_time_stamp  # type: int
        self.option_list = option_list  # type: str
        self.live_video_summary = live_video_summary  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.start_time_stamp, 'start_time_stamp')
        self.validate_required(self.end_time_stamp, 'end_time_stamp')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['DeviceId'] = self.device_id
        result['StartTimeStamp'] = self.start_time_stamp
        result['EndTimeStamp'] = self.end_time_stamp
        result['OptionList'] = self.option_list
        result['LiveVideoSummary'] = self.live_video_summary
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.device_id = map.get('DeviceId')
        self.start_time_stamp = map.get('StartTimeStamp')
        self.end_time_stamp = map.get('EndTimeStamp')
        self.option_list = map.get('OptionList')
        self.live_video_summary = map.get('LiveVideoSummary')
        return self


class CreateVideoSummaryTaskResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class ListMotorAlgorithmResultsRequest(TeaModel):
    def __init__(self, corp_id=None, algorithm_type=None, data_source_id=None, start_time=None, end_time=None,
                 page_number=None, page_size=None, plate_number=None):
        self.corp_id = corp_id          # type: str
        self.algorithm_type = algorithm_type  # type: str
        self.data_source_id = data_source_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.plate_number = plate_number  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.algorithm_type, 'algorithm_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['AlgorithmType'] = self.algorithm_type
        result['DataSourceId'] = self.data_source_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['PlateNumber'] = self.plate_number
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.algorithm_type = map.get('AlgorithmType')
        self.data_source_id = map.get('DataSourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.plate_number = map.get('PlateNumber')
        return self


class ListMotorAlgorithmResultsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListMotorAlgorithmResultsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListMotorAlgorithmResultsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListMotorAlgorithmResultsResponseDataRecords(TeaModel):
    def __init__(self, corp_id=None, data_source_id=None, left_top_x=None, left_top_y=None, motor_id=None,
                 pic_url_path=None, plate_number=None, right_bottom_x=None, right_bottom_y=None, shot_time=None,
                 target_pic_url_path=None, motor_style=None, motor_model=None, motor_color=None, motor_class=None, motor_brand=None,
                 plate_color=None, plate_class=None, safety_belt=None, calling=None, source_id=None):
        self.corp_id = corp_id          # type: str
        self.data_source_id = data_source_id  # type: str
        self.left_top_x = left_top_x    # type: float
        self.left_top_y = left_top_y    # type: float
        self.motor_id = motor_id        # type: str
        self.pic_url_path = pic_url_path  # type: str
        self.plate_number = plate_number  # type: str
        self.right_bottom_x = right_bottom_x  # type: float
        self.right_bottom_y = right_bottom_y  # type: float
        self.shot_time = shot_time      # type: str
        self.target_pic_url_path = target_pic_url_path  # type: str
        self.motor_style = motor_style  # type: str
        self.motor_model = motor_model  # type: str
        self.motor_color = motor_color  # type: str
        self.motor_class = motor_class  # type: str
        self.motor_brand = motor_brand  # type: str
        self.plate_color = plate_color  # type: str
        self.plate_class = plate_class  # type: str
        self.safety_belt = safety_belt  # type: str
        self.calling = calling          # type: str
        self.source_id = source_id      # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.data_source_id, 'data_source_id')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.motor_id, 'motor_id')
        self.validate_required(self.pic_url_path, 'pic_url_path')
        self.validate_required(self.plate_number, 'plate_number')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.target_pic_url_path, 'target_pic_url_path')
        self.validate_required(self.motor_style, 'motor_style')
        self.validate_required(self.motor_model, 'motor_model')
        self.validate_required(self.motor_color, 'motor_color')
        self.validate_required(self.motor_class, 'motor_class')
        self.validate_required(self.motor_brand, 'motor_brand')
        self.validate_required(self.plate_color, 'plate_color')
        self.validate_required(self.plate_class, 'plate_class')
        self.validate_required(self.safety_belt, 'safety_belt')
        self.validate_required(self.calling, 'calling')
        self.validate_required(self.source_id, 'source_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['DataSourceId'] = self.data_source_id
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['MotorId'] = self.motor_id
        result['PicUrlPath'] = self.pic_url_path
        result['PlateNumber'] = self.plate_number
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['ShotTime'] = self.shot_time
        result['TargetPicUrlPath'] = self.target_pic_url_path
        result['MotorStyle'] = self.motor_style
        result['MotorModel'] = self.motor_model
        result['MotorColor'] = self.motor_color
        result['MotorClass'] = self.motor_class
        result['MotorBrand'] = self.motor_brand
        result['PlateColor'] = self.plate_color
        result['PlateClass'] = self.plate_class
        result['SafetyBelt'] = self.safety_belt
        result['Calling'] = self.calling
        result['SourceId'] = self.source_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.data_source_id = map.get('DataSourceId')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.motor_id = map.get('MotorId')
        self.pic_url_path = map.get('PicUrlPath')
        self.plate_number = map.get('PlateNumber')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.shot_time = map.get('ShotTime')
        self.target_pic_url_path = map.get('TargetPicUrlPath')
        self.motor_style = map.get('MotorStyle')
        self.motor_model = map.get('MotorModel')
        self.motor_color = map.get('MotorColor')
        self.motor_class = map.get('MotorClass')
        self.motor_brand = map.get('MotorBrand')
        self.plate_color = map.get('PlateColor')
        self.plate_class = map.get('PlateClass')
        self.safety_belt = map.get('SafetyBelt')
        self.calling = map.get('Calling')
        self.source_id = map.get('SourceId')
        return self


class ListMotorAlgorithmResultsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[ListMotorAlgorithmResultsResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListMotorAlgorithmResultsResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class ListFaceAlgorithmResultsRequest(TeaModel):
    def __init__(self, corp_id=None, algorithm_type=None, data_source_id=None, start_time=None, end_time=None,
                 page_number=None, page_size=None):
        self.corp_id = corp_id          # type: str
        self.algorithm_type = algorithm_type  # type: str
        self.data_source_id = data_source_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.algorithm_type, 'algorithm_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['AlgorithmType'] = self.algorithm_type
        result['DataSourceId'] = self.data_source_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.algorithm_type = map.get('AlgorithmType')
        self.data_source_id = map.get('DataSourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListFaceAlgorithmResultsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListFaceAlgorithmResultsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListFaceAlgorithmResultsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListFaceAlgorithmResultsResponseDataRecords(TeaModel):
    def __init__(self, face_id=None, corp_id=None, data_source_id=None, shot_time=None, gender_code=None,
                 min_age=None, max_age=None, cap_style=None, hair_style=None, left_top_x=None, left_top_y=None,
                 right_bottom_x=None, right_bottom_y=None, pic_url_path=None, target_pic_url_path=None, source_id=None):
        self.face_id = face_id          # type: str
        self.corp_id = corp_id          # type: str
        self.data_source_id = data_source_id  # type: str
        self.shot_time = shot_time      # type: str
        self.gender_code = gender_code  # type: str
        self.min_age = min_age          # type: str
        self.max_age = max_age          # type: str
        self.cap_style = cap_style      # type: str
        self.hair_style = hair_style    # type: str
        self.left_top_x = left_top_x    # type: float
        self.left_top_y = left_top_y    # type: float
        self.right_bottom_x = right_bottom_x  # type: float
        self.right_bottom_y = right_bottom_y  # type: float
        self.pic_url_path = pic_url_path  # type: str
        self.target_pic_url_path = target_pic_url_path  # type: str
        self.source_id = source_id      # type: str

    def validate(self):
        self.validate_required(self.face_id, 'face_id')
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.data_source_id, 'data_source_id')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.gender_code, 'gender_code')
        self.validate_required(self.min_age, 'min_age')
        self.validate_required(self.max_age, 'max_age')
        self.validate_required(self.cap_style, 'cap_style')
        self.validate_required(self.hair_style, 'hair_style')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.pic_url_path, 'pic_url_path')
        self.validate_required(self.target_pic_url_path, 'target_pic_url_path')
        self.validate_required(self.source_id, 'source_id')

    def to_map(self):
        result = {}
        result['FaceId'] = self.face_id
        result['CorpId'] = self.corp_id
        result['DataSourceId'] = self.data_source_id
        result['ShotTime'] = self.shot_time
        result['GenderCode'] = self.gender_code
        result['MinAge'] = self.min_age
        result['MaxAge'] = self.max_age
        result['CapStyle'] = self.cap_style
        result['HairStyle'] = self.hair_style
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['PicUrlPath'] = self.pic_url_path
        result['TargetPicUrlPath'] = self.target_pic_url_path
        result['SourceId'] = self.source_id
        return result

    def from_map(self, map={}):
        self.face_id = map.get('FaceId')
        self.corp_id = map.get('CorpId')
        self.data_source_id = map.get('DataSourceId')
        self.shot_time = map.get('ShotTime')
        self.gender_code = map.get('GenderCode')
        self.min_age = map.get('MinAge')
        self.max_age = map.get('MaxAge')
        self.cap_style = map.get('CapStyle')
        self.hair_style = map.get('HairStyle')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.pic_url_path = map.get('PicUrlPath')
        self.target_pic_url_path = map.get('TargetPicUrlPath')
        self.source_id = map.get('SourceId')
        return self


class ListFaceAlgorithmResultsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[ListFaceAlgorithmResultsResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListFaceAlgorithmResultsResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class ListMetricsRequest(TeaModel):
    def __init__(self, corp_id=None, tag_code=None, aggregate_type=None, start_time=None, end_time=None,
                 page_number=None, page_size=None):
        self.corp_id = corp_id          # type: str
        self.tag_code = tag_code        # type: str
        self.aggregate_type = aggregate_type  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.aggregate_type, 'aggregate_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TagCode'] = self.tag_code
        result['AggregateType'] = self.aggregate_type
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.tag_code = map.get('TagCode')
        self.aggregate_type = map.get('AggregateType')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListMetricsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListMetricsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListMetricsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListMetricsResponseDataRecords(TeaModel):
    def __init__(self, date_time=None, tag_code=None, tag_value=None, tag_metric=None):
        self.date_time = date_time      # type: str
        self.tag_code = tag_code        # type: str
        self.tag_value = tag_value      # type: str
        self.tag_metric = tag_metric    # type: str

    def validate(self):
        self.validate_required(self.date_time, 'date_time')
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.tag_metric, 'tag_metric')

    def to_map(self):
        result = {}
        result['DateTime'] = self.date_time
        result['TagCode'] = self.tag_code
        result['TagValue'] = self.tag_value
        result['TagMetric'] = self.tag_metric
        return result

    def from_map(self, map={}):
        self.date_time = map.get('DateTime')
        self.tag_code = map.get('TagCode')
        self.tag_value = map.get('TagValue')
        self.tag_metric = map.get('TagMetric')
        return self


class ListMetricsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[ListMetricsResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListMetricsResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class DeleteRecordsRequest(TeaModel):
    def __init__(self, corp_id=None, algorithm_type=None, attribute_name=None, operator_type=None, value=None):
        self.corp_id = corp_id          # type: str
        self.algorithm_type = algorithm_type  # type: str
        self.attribute_name = attribute_name  # type: str
        self.operator_type = operator_type  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['AlgorithmType'] = self.algorithm_type
        result['AttributeName'] = self.attribute_name
        result['OperatorType'] = self.operator_type
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.algorithm_type = map.get('AlgorithmType')
        self.attribute_name = map.get('AttributeName')
        self.operator_type = map.get('OperatorType')
        self.value = map.get('Value')
        return self


class DeleteRecordsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class RecognizeFaceQualityRequest(TeaModel):
    def __init__(self, corp_id=None, pic_content=None, pic_format=None, pic_url=None):
        self.corp_id = corp_id          # type: str
        self.pic_content = pic_content  # type: str
        self.pic_format = pic_format    # type: str
        self.pic_url = pic_url          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PicContent'] = self.pic_content
        result['PicFormat'] = self.pic_format
        result['PicUrl'] = self.pic_url
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.pic_content = map.get('PicContent')
        self.pic_format = map.get('PicFormat')
        self.pic_url = map.get('PicUrl')
        return self


class RecognizeFaceQualityResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeFaceQualityResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeFaceQualityResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeFaceQualityResponseDataAttributes(TeaModel):
    def __init__(self, left_top_x=None, left_top_y=None, right_bottom_x=None, right_bottom_y=None,
                 target_image_storage_path=None, face_style=None, face_quality=None, face_score=None):
        self.left_top_x = left_top_x    # type: int
        self.left_top_y = left_top_y    # type: int
        self.right_bottom_x = right_bottom_x  # type: int
        self.right_bottom_y = right_bottom_y  # type: int
        self.target_image_storage_path = target_image_storage_path  # type: str
        self.face_style = face_style    # type: str
        self.face_quality = face_quality  # type: str
        self.face_score = face_score    # type: str

    def validate(self):
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.target_image_storage_path, 'target_image_storage_path')
        self.validate_required(self.face_style, 'face_style')
        self.validate_required(self.face_quality, 'face_quality')
        self.validate_required(self.face_score, 'face_score')

    def to_map(self):
        result = {}
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['TargetImageStoragePath'] = self.target_image_storage_path
        result['FaceStyle'] = self.face_style
        result['FaceQuality'] = self.face_quality
        result['FaceScore'] = self.face_score
        return result

    def from_map(self, map={}):
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.target_image_storage_path = map.get('TargetImageStoragePath')
        self.face_style = map.get('FaceStyle')
        self.face_quality = map.get('FaceQuality')
        self.face_score = map.get('FaceScore')
        return self


class RecognizeFaceQualityResponseData(TeaModel):
    def __init__(self, quality_score=None, description=None, attributes=None):
        self.quality_score = quality_score  # type: str
        self.description = description  # type: str
        self.attributes = attributes    # type: RecognizeFaceQualityResponseDataAttributes

    def validate(self):
        self.validate_required(self.quality_score, 'quality_score')
        self.validate_required(self.description, 'description')
        self.validate_required(self.attributes, 'attributes')
        if self.attributes:
            self.attributes.validate()

    def to_map(self):
        result = {}
        result['QualityScore'] = self.quality_score
        result['Description'] = self.description
        if self.attributes is not None:
            result['Attributes'] = self.attributes.to_map()
        else:
            result['Attributes'] = None
        return result

    def from_map(self, map={}):
        self.quality_score = map.get('QualityScore')
        self.description = map.get('Description')
        if map.get('Attributes') is not None:
            temp_model = RecognizeFaceQualityResponseDataAttributes()
            self.attributes = temp_model.from_map(map['Attributes'])
        else:
            self.attributes = None
        return self


class ListPersonsRequest(TeaModel):
    def __init__(self, corp_id=None, page_no=None, page_size=None, start_time=None, end_time=None,
                 algorithm_type=None):
        self.corp_id = corp_id          # type: str
        self.page_no = page_no          # type: str
        self.page_size = page_size      # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.algorithm_type = algorithm_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['AlgorithmType'] = self.algorithm_type
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.algorithm_type = map.get('AlgorithmType')
        return self


class ListPersonsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListPersonsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListPersonsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListPersonsResponseDataRecordsTagList(TeaModel):
    def __init__(self, tag_code=None, tag_name=None, tag_value=None, tag_value_id=None):
        self.tag_code = tag_code        # type: str
        self.tag_name = tag_name        # type: str
        self.tag_value = tag_value      # type: str
        self.tag_value_id = tag_value_id  # type: str

    def validate(self):
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.tag_name, 'tag_name')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.tag_value_id, 'tag_value_id')

    def to_map(self):
        result = {}
        result['TagCode'] = self.tag_code
        result['TagName'] = self.tag_name
        result['TagValue'] = self.tag_value
        result['TagValueId'] = self.tag_value_id
        return result

    def from_map(self, map={}):
        self.tag_code = map.get('TagCode')
        self.tag_name = map.get('TagName')
        self.tag_value = map.get('TagValue')
        self.tag_value_id = map.get('TagValueId')
        return self


class ListPersonsResponseDataRecords(TeaModel):
    def __init__(self, first_appear_time=None, person_id=None, pic_url=None, tag_list=None):
        self.first_appear_time = first_appear_time  # type: str
        self.person_id = person_id      # type: str
        self.pic_url = pic_url          # type: str
        self.tag_list = tag_list        # type: List[ListPersonsResponseDataRecordsTagList]

    def validate(self):
        self.validate_required(self.first_appear_time, 'first_appear_time')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.pic_url, 'pic_url')
        self.validate_required(self.tag_list, 'tag_list')
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FirstAppearTime'] = self.first_appear_time
        result['PersonId'] = self.person_id
        result['PicUrl'] = self.pic_url
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        else:
            result['TagList'] = None
        return result

    def from_map(self, map={}):
        self.first_appear_time = map.get('FirstAppearTime')
        self.person_id = map.get('PersonId')
        self.pic_url = map.get('PicUrl')
        self.tag_list = []
        if map.get('TagList') is not None:
            for k in map.get('TagList'):
                temp_model = ListPersonsResponseDataRecordsTagList()
                self.tag_list.append(temp_model.from_map(k))
        else:
            self.tag_list = None
        return self


class ListPersonsResponseData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_no = page_no          # type: str
        self.page_size = page_size      # type: str
        self.total_count = total_count  # type: str
        self.total_page = total_page    # type: str
        self.records = records          # type: List[ListPersonsResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListPersonsResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class GetPersonDetailRequest(TeaModel):
    def __init__(self, corp_id=None, person_id=None, algorithm_type=None):
        self.corp_id = corp_id          # type: str
        self.person_id = person_id      # type: str
        self.algorithm_type = algorithm_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PersonID'] = self.person_id
        result['AlgorithmType'] = self.algorithm_type
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.person_id = map.get('PersonID')
        self.algorithm_type = map.get('AlgorithmType')
        return self


class GetPersonDetailResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetPersonDetailResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetPersonDetailResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetPersonDetailResponseDataTagList(TeaModel):
    def __init__(self, tag_code=None, tag_name=None, tag_value=None, tag_value_id=None):
        self.tag_code = tag_code        # type: str
        self.tag_name = tag_name        # type: str
        self.tag_value = tag_value      # type: str
        self.tag_value_id = tag_value_id  # type: str

    def validate(self):
        self.validate_required(self.tag_code, 'tag_code')
        self.validate_required(self.tag_name, 'tag_name')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.tag_value_id, 'tag_value_id')

    def to_map(self):
        result = {}
        result['TagCode'] = self.tag_code
        result['TagName'] = self.tag_name
        result['TagValue'] = self.tag_value
        result['TagValueId'] = self.tag_value_id
        return result

    def from_map(self, map={}):
        self.tag_code = map.get('TagCode')
        self.tag_name = map.get('TagName')
        self.tag_value = map.get('TagValue')
        self.tag_value_id = map.get('TagValueId')
        return self


class GetPersonDetailResponseData(TeaModel):
    def __init__(self, pic_url=None, person_id=None, tag_list=None):
        self.pic_url = pic_url          # type: str
        self.person_id = person_id      # type: str
        self.tag_list = tag_list        # type: List[GetPersonDetailResponseDataTagList]

    def validate(self):
        self.validate_required(self.pic_url, 'pic_url')
        self.validate_required(self.person_id, 'person_id')
        self.validate_required(self.tag_list, 'tag_list')
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PicUrl'] = self.pic_url
        result['PersonId'] = self.person_id
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        else:
            result['TagList'] = None
        return result

    def from_map(self, map={}):
        self.pic_url = map.get('PicUrl')
        self.person_id = map.get('PersonId')
        self.tag_list = []
        if map.get('TagList') is not None:
            for k in map.get('TagList'):
                temp_model = GetPersonDetailResponseDataTagList()
                self.tag_list.append(temp_model.from_map(k))
        else:
            self.tag_list = None
        return self


class GetFaceOptionsRequest(TeaModel):
    def __init__(self, corp_id=None):
        self.corp_id = corp_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        return self


class GetFaceOptionsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetFaceOptionsResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetFaceOptionsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetFaceOptionsResponseDataOptionList(TeaModel):
    def __init__(self, key=None, name=None):
        self.key = key                  # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.name = map.get('Name')
        return self


class GetFaceOptionsResponseData(TeaModel):
    def __init__(self, key=None, name=None, option_list=None):
        self.key = key                  # type: str
        self.name = name                # type: str
        self.option_list = option_list  # type: List[GetFaceOptionsResponseDataOptionList]

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.name, 'name')
        self.validate_required(self.option_list, 'option_list')
        if self.option_list:
            for k in self.option_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Name'] = self.name
        result['OptionList'] = []
        if self.option_list is not None:
            for k in self.option_list:
                result['OptionList'].append(k.to_map() if k else None)
        else:
            result['OptionList'] = None
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.name = map.get('Name')
        self.option_list = []
        if map.get('OptionList') is not None:
            for k in map.get('OptionList'):
                temp_model = GetFaceOptionsResponseDataOptionList()
                self.option_list.append(temp_model.from_map(k))
        else:
            self.option_list = None
        return self


class GetBodyOptionsRequest(TeaModel):
    def __init__(self, corp_id=None):
        self.corp_id = corp_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        return self


class GetBodyOptionsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetBodyOptionsResponseData]

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetBodyOptionsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetBodyOptionsResponseDataOptionList(TeaModel):
    def __init__(self, key=None, name=None):
        self.key = key                  # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.name = map.get('Name')
        return self


class GetBodyOptionsResponseData(TeaModel):
    def __init__(self, key=None, name=None, option_list=None):
        self.key = key                  # type: str
        self.name = name                # type: str
        self.option_list = option_list  # type: List[GetBodyOptionsResponseDataOptionList]

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.name, 'name')
        self.validate_required(self.option_list, 'option_list')
        if self.option_list:
            for k in self.option_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Name'] = self.name
        result['OptionList'] = []
        if self.option_list is not None:
            for k in self.option_list:
                result['OptionList'].append(k.to_map() if k else None)
        else:
            result['OptionList'] = None
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.name = map.get('Name')
        self.option_list = []
        if map.get('OptionList') is not None:
            for k in map.get('OptionList'):
                temp_model = GetBodyOptionsResponseDataOptionList()
                self.option_list.append(temp_model.from_map(k))
        else:
            self.option_list = None
        return self


class StopMonitorRequest(TeaModel):
    def __init__(self, task_id=None, algorithm_vendor=None):
        self.task_id = task_id          # type: str
        self.algorithm_vendor = algorithm_vendor  # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.algorithm_vendor, 'algorithm_vendor')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.algorithm_vendor = map.get('AlgorithmVendor')
        return self


class StopMonitorResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class SearchBodyRequest(TeaModel):
    def __init__(self, corp_id=None, gb_id=None, start_time_stamp=None, end_time_stamp=None, page_no=None,
                 page_size=None, option_list=None):
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str
        self.start_time_stamp = start_time_stamp  # type: int
        self.end_time_stamp = end_time_stamp  # type: int
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.option_list = option_list  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.start_time_stamp, 'start_time_stamp')
        self.validate_required(self.end_time_stamp, 'end_time_stamp')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        result['StartTimeStamp'] = self.start_time_stamp
        result['EndTimeStamp'] = self.end_time_stamp
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['OptionList'] = self.option_list
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        self.start_time_stamp = map.get('StartTimeStamp')
        self.end_time_stamp = map.get('EndTimeStamp')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.option_list = map.get('OptionList')
        return self


class SearchBodyShrinkRequest(TeaModel):
    def __init__(self, corp_id=None, gb_id=None, start_time_stamp=None, end_time_stamp=None, page_no=None,
                 page_size=None, option_list_shrink=None):
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str
        self.start_time_stamp = start_time_stamp  # type: int
        self.end_time_stamp = end_time_stamp  # type: int
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.option_list_shrink = option_list_shrink  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.start_time_stamp, 'start_time_stamp')
        self.validate_required(self.end_time_stamp, 'end_time_stamp')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        result['StartTimeStamp'] = self.start_time_stamp
        result['EndTimeStamp'] = self.end_time_stamp
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['OptionList'] = self.option_list_shrink
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        self.start_time_stamp = map.get('StartTimeStamp')
        self.end_time_stamp = map.get('EndTimeStamp')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.option_list_shrink = map.get('OptionList')
        return self


class SearchBodyResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: SearchBodyResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SearchBodyResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class SearchBodyResponseDataRecords(TeaModel):
    def __init__(self, gb_id=None, image_url=None, left_top_x=None, left_top_y=None, right_bottom_x=None,
                 right_bottom_y=None, score=None, target_image_url=None):
        self.gb_id = gb_id              # type: str
        self.image_url = image_url      # type: str
        self.left_top_x = left_top_x    # type: float
        self.left_top_y = left_top_y    # type: float
        self.right_bottom_x = right_bottom_x  # type: float
        self.right_bottom_y = right_bottom_y  # type: float
        self.score = score              # type: float
        self.target_image_url = target_image_url  # type: str

    def validate(self):
        self.validate_required(self.gb_id, 'gb_id')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.score, 'score')
        self.validate_required(self.target_image_url, 'target_image_url')

    def to_map(self):
        result = {}
        result['GbId'] = self.gb_id
        result['ImageUrl'] = self.image_url
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['Score'] = self.score
        result['TargetImageUrl'] = self.target_image_url
        return result

    def from_map(self, map={}):
        self.gb_id = map.get('GbId')
        self.image_url = map.get('ImageUrl')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.score = map.get('Score')
        self.target_image_url = map.get('TargetImageUrl')
        return self


class SearchBodyResponseData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[SearchBodyResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = SearchBodyResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class AddMonitorRequest(TeaModel):
    def __init__(self, corp_id=None, monitor_type=None, description=None, batch_indicator=None,
                 algorithm_vendor=None, notifier_type=None, notifier_url=None, notifier_app_secret=None, notifier_time_out=None,
                 notifier_extend_values=None):
        self.corp_id = corp_id          # type: str
        self.monitor_type = monitor_type  # type: str
        self.description = description  # type: str
        self.batch_indicator = batch_indicator  # type: int
        self.algorithm_vendor = algorithm_vendor  # type: str
        self.notifier_type = notifier_type  # type: str
        self.notifier_url = notifier_url  # type: str
        self.notifier_app_secret = notifier_app_secret  # type: str
        self.notifier_time_out = notifier_time_out  # type: int
        self.notifier_extend_values = notifier_extend_values  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.monitor_type, 'monitor_type')
        self.validate_required(self.algorithm_vendor, 'algorithm_vendor')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['MonitorType'] = self.monitor_type
        result['Description'] = self.description
        result['BatchIndicator'] = self.batch_indicator
        result['AlgorithmVendor'] = self.algorithm_vendor
        result['NotifierType'] = self.notifier_type
        result['NotifierUrl'] = self.notifier_url
        result['NotifierAppSecret'] = self.notifier_app_secret
        result['NotifierTimeOut'] = self.notifier_time_out
        result['NotifierExtendValues'] = self.notifier_extend_values
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.monitor_type = map.get('MonitorType')
        self.description = map.get('Description')
        self.batch_indicator = map.get('BatchIndicator')
        self.algorithm_vendor = map.get('AlgorithmVendor')
        self.notifier_type = map.get('NotifierType')
        self.notifier_url = map.get('NotifierUrl')
        self.notifier_app_secret = map.get('NotifierAppSecret')
        self.notifier_time_out = map.get('NotifierTimeOut')
        self.notifier_extend_values = map.get('NotifierExtendValues')
        return self


class AddMonitorResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: AddMonitorResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = AddMonitorResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class AddMonitorResponseData(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        return self


class GetMonitorResultRequest(TeaModel):
    def __init__(self, corp_id=None, task_id=None, min_record_id=None, start_time=None, end_time=None,
                 algorithm_vendor=None):
        self.corp_id = corp_id          # type: str
        self.task_id = task_id          # type: str
        self.min_record_id = min_record_id  # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.algorithm_vendor = algorithm_vendor  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TaskId'] = self.task_id
        result['MinRecordId'] = self.min_record_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['AlgorithmVendor'] = self.algorithm_vendor
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.task_id = map.get('TaskId')
        self.min_record_id = map.get('MinRecordId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.algorithm_vendor = map.get('AlgorithmVendor')
        return self


class GetMonitorResultResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: GetMonitorResultResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetMonitorResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetMonitorResultResponseDataRecordsExtendInfo(TeaModel):
    def __init__(self, plate_no=None):
        self.plate_no = plate_no        # type: str

    def validate(self):
        self.validate_required(self.plate_no, 'plate_no')

    def to_map(self):
        result = {}
        result['PlateNo'] = self.plate_no
        return result

    def from_map(self, map={}):
        self.plate_no = map.get('PlateNo')
        return self


class GetMonitorResultResponseDataRecords(TeaModel):
    def __init__(self, right_bottom_y=None, right_bottom_x=None, left_up_y=None, left_up_x=None, gb_id=None,
                 score=None, pic_url=None, shot_time=None, monitor_pic_url=None, target_pic_url=None, task_id=None,
                 extend_info=None):
        self.right_bottom_y = right_bottom_y  # type: str
        self.right_bottom_x = right_bottom_x  # type: str
        self.left_up_y = left_up_y      # type: str
        self.left_up_x = left_up_x      # type: str
        self.gb_id = gb_id              # type: str
        self.score = score              # type: str
        self.pic_url = pic_url          # type: str
        self.shot_time = shot_time      # type: str
        self.monitor_pic_url = monitor_pic_url  # type: str
        self.target_pic_url = target_pic_url  # type: str
        self.task_id = task_id          # type: str
        self.extend_info = extend_info  # type: GetMonitorResultResponseDataRecordsExtendInfo

    def validate(self):
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.left_up_y, 'left_up_y')
        self.validate_required(self.left_up_x, 'left_up_x')
        self.validate_required(self.gb_id, 'gb_id')
        self.validate_required(self.score, 'score')
        self.validate_required(self.pic_url, 'pic_url')
        self.validate_required(self.shot_time, 'shot_time')
        self.validate_required(self.monitor_pic_url, 'monitor_pic_url')
        self.validate_required(self.target_pic_url, 'target_pic_url')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.extend_info, 'extend_info')
        if self.extend_info:
            self.extend_info.validate()

    def to_map(self):
        result = {}
        result['RightBottomY'] = self.right_bottom_y
        result['RightBottomX'] = self.right_bottom_x
        result['LeftUpY'] = self.left_up_y
        result['LeftUpX'] = self.left_up_x
        result['GbId'] = self.gb_id
        result['Score'] = self.score
        result['PicUrl'] = self.pic_url
        result['ShotTime'] = self.shot_time
        result['MonitorPicUrl'] = self.monitor_pic_url
        result['TargetPicUrl'] = self.target_pic_url
        result['TaskId'] = self.task_id
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info.to_map()
        else:
            result['ExtendInfo'] = None
        return result

    def from_map(self, map={}):
        self.right_bottom_y = map.get('RightBottomY')
        self.right_bottom_x = map.get('RightBottomX')
        self.left_up_y = map.get('LeftUpY')
        self.left_up_x = map.get('LeftUpX')
        self.gb_id = map.get('GbId')
        self.score = map.get('Score')
        self.pic_url = map.get('PicUrl')
        self.shot_time = map.get('ShotTime')
        self.monitor_pic_url = map.get('MonitorPicUrl')
        self.target_pic_url = map.get('TargetPicUrl')
        self.task_id = map.get('TaskId')
        if map.get('ExtendInfo') is not None:
            temp_model = GetMonitorResultResponseDataRecordsExtendInfo()
            self.extend_info = temp_model.from_map(map['ExtendInfo'])
        else:
            self.extend_info = None
        return self


class GetMonitorResultResponseData(TeaModel):
    def __init__(self, max_id=None, records=None):
        self.max_id = max_id            # type: str
        self.records = records          # type: List[GetMonitorResultResponseDataRecords]

    def validate(self):
        self.validate_required(self.max_id, 'max_id')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MaxId'] = self.max_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.max_id = map.get('MaxId')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = GetMonitorResultResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class UpdateMonitorRequest(TeaModel):
    def __init__(self, corp_id=None, task_id=None, rule_name=None, device_operate_type=None, device_list=None,
                 pic_operate_type=None, pic_list=None, attribute_operate_type=None, attribute_name=None, attribute_value_list=None,
                 description=None, rule_expression=None, algorithm_vendor=None, notifier_type=None, notifier_url=None,
                 notifier_app_secret=None, notifier_time_out=None, notifier_extend_values=None):
        self.corp_id = corp_id          # type: str
        self.task_id = task_id          # type: str
        self.rule_name = rule_name      # type: str
        self.device_operate_type = device_operate_type  # type: str
        self.device_list = device_list  # type: str
        self.pic_operate_type = pic_operate_type  # type: str
        self.pic_list = pic_list        # type: str
        self.attribute_operate_type = attribute_operate_type  # type: str
        self.attribute_name = attribute_name  # type: str
        self.attribute_value_list = attribute_value_list  # type: str
        self.description = description  # type: str
        self.rule_expression = rule_expression  # type: str
        self.algorithm_vendor = algorithm_vendor  # type: str
        self.notifier_type = notifier_type  # type: str
        self.notifier_url = notifier_url  # type: str
        self.notifier_app_secret = notifier_app_secret  # type: str
        self.notifier_time_out = notifier_time_out  # type: int
        self.notifier_extend_values = notifier_extend_values  # type: str

    def validate(self):
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.algorithm_vendor, 'algorithm_vendor')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['TaskId'] = self.task_id
        result['RuleName'] = self.rule_name
        result['DeviceOperateType'] = self.device_operate_type
        result['DeviceList'] = self.device_list
        result['PicOperateType'] = self.pic_operate_type
        result['PicList'] = self.pic_list
        result['AttributeOperateType'] = self.attribute_operate_type
        result['AttributeName'] = self.attribute_name
        result['AttributeValueList'] = self.attribute_value_list
        result['Description'] = self.description
        result['RuleExpression'] = self.rule_expression
        result['AlgorithmVendor'] = self.algorithm_vendor
        result['NotifierType'] = self.notifier_type
        result['NotifierUrl'] = self.notifier_url
        result['NotifierAppSecret'] = self.notifier_app_secret
        result['NotifierTimeOut'] = self.notifier_time_out
        result['NotifierExtendValues'] = self.notifier_extend_values
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.task_id = map.get('TaskId')
        self.rule_name = map.get('RuleName')
        self.device_operate_type = map.get('DeviceOperateType')
        self.device_list = map.get('DeviceList')
        self.pic_operate_type = map.get('PicOperateType')
        self.pic_list = map.get('PicList')
        self.attribute_operate_type = map.get('AttributeOperateType')
        self.attribute_name = map.get('AttributeName')
        self.attribute_value_list = map.get('AttributeValueList')
        self.description = map.get('Description')
        self.rule_expression = map.get('RuleExpression')
        self.algorithm_vendor = map.get('AlgorithmVendor')
        self.notifier_type = map.get('NotifierType')
        self.notifier_url = map.get('NotifierUrl')
        self.notifier_app_secret = map.get('NotifierAppSecret')
        self.notifier_time_out = map.get('NotifierTimeOut')
        self.notifier_extend_values = map.get('NotifierExtendValues')
        return self


class UpdateMonitorResponse(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        return self


class GetDeviceVideoUrlRequest(TeaModel):
    def __init__(self, corp_id=None, gb_id=None, start_time=None, end_time=None, device_id=None, out_protocol=None):
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.device_id = device_id      # type: str
        self.out_protocol = out_protocol  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DeviceId'] = self.device_id
        result['OutProtocol'] = self.out_protocol
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.device_id = map.get('DeviceId')
        self.out_protocol = map.get('OutProtocol')
        return self


class GetDeviceVideoUrlResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, url=None, out_protocol=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.url = url                  # type: str
        self.out_protocol = out_protocol  # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.url, 'url')
        self.validate_required(self.out_protocol, 'out_protocol')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Url'] = self.url
        result['OutProtocol'] = self.out_protocol
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.url = map.get('Url')
        self.out_protocol = map.get('OutProtocol')
        return self


class GetInventoryRequest(TeaModel):
    def __init__(self, commodity_code=None):
        self.commodity_code = commodity_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, map={}):
        self.commodity_code = map.get('CommodityCode')
        return self


class GetInventoryResponse(TeaModel):
    def __init__(self, success=None, data=None):
        self.success = success          # type: bool
        self.data = data                # type: GetInventoryResponseData

    def validate(self):
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetInventoryResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetInventoryResponseDataResultObject(TeaModel):
    def __init__(self, buyer_id=None, commodity_code=None, current_inventory=None, valid_end_time=None,
                 valid_start_time=None, instance_id=None, inventory_id=None):
        self.buyer_id = buyer_id        # type: str
        self.commodity_code = commodity_code  # type: str
        self.current_inventory = current_inventory  # type: str
        self.valid_end_time = valid_end_time  # type: str
        self.valid_start_time = valid_start_time  # type: str
        self.instance_id = instance_id  # type: str
        self.inventory_id = inventory_id  # type: str

    def validate(self):
        self.validate_required(self.buyer_id, 'buyer_id')
        self.validate_required(self.commodity_code, 'commodity_code')
        self.validate_required(self.current_inventory, 'current_inventory')
        self.validate_required(self.valid_end_time, 'valid_end_time')
        self.validate_required(self.valid_start_time, 'valid_start_time')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.inventory_id, 'inventory_id')

    def to_map(self):
        result = {}
        result['BuyerId'] = self.buyer_id
        result['CommodityCode'] = self.commodity_code
        result['CurrentInventory'] = self.current_inventory
        result['ValidEndTime'] = self.valid_end_time
        result['ValidStartTime'] = self.valid_start_time
        result['InstanceId'] = self.instance_id
        result['InventoryId'] = self.inventory_id
        return result

    def from_map(self, map={}):
        self.buyer_id = map.get('BuyerId')
        self.commodity_code = map.get('CommodityCode')
        self.current_inventory = map.get('CurrentInventory')
        self.valid_end_time = map.get('ValidEndTime')
        self.valid_start_time = map.get('ValidStartTime')
        self.instance_id = map.get('InstanceId')
        self.inventory_id = map.get('InventoryId')
        return self


class GetInventoryResponseData(TeaModel):
    def __init__(self, result_object=None):
        self.result_object = result_object  # type: List[GetInventoryResponseDataResultObject]

    def validate(self):
        self.validate_required(self.result_object, 'result_object')
        if self.result_object:
            for k in self.result_object:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResultObject'] = []
        if self.result_object is not None:
            for k in self.result_object:
                result['ResultObject'].append(k.to_map() if k else None)
        else:
            result['ResultObject'] = None
        return result

    def from_map(self, map={}):
        self.result_object = []
        if map.get('ResultObject') is not None:
            for k in map.get('ResultObject'):
                temp_model = GetInventoryResponseDataResultObject()
                self.result_object.append(temp_model.from_map(k))
        else:
            self.result_object = None
        return self


class RecognizeImageRequest(TeaModel):
    def __init__(self, corp_id=None, pic_content=None, pic_format=None, pic_url=None):
        self.corp_id = corp_id          # type: str
        self.pic_content = pic_content  # type: str
        self.pic_format = pic_format    # type: str
        self.pic_url = pic_url          # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.pic_format, 'pic_format')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['PicContent'] = self.pic_content
        result['PicFormat'] = self.pic_format
        result['PicUrl'] = self.pic_url
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.pic_content = map.get('PicContent')
        self.pic_format = map.get('PicFormat')
        self.pic_url = map.get('PicUrl')
        return self


class RecognizeImageResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: RecognizeImageResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = RecognizeImageResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class RecognizeImageResponseDataBodyList(TeaModel):
    def __init__(self, feature=None, file_name=None, image_base_six_four=None, left_top_x=None, left_top_y=None,
                 local_feature=None, respirator_color=None, right_bottom_x=None, right_bottom_y=None):
        self.feature = feature          # type: str
        self.file_name = file_name      # type: str
        self.image_base_six_four = image_base_six_four  # type: str
        self.left_top_x = left_top_x    # type: str
        self.left_top_y = left_top_y    # type: str
        self.local_feature = local_feature  # type: str
        self.respirator_color = respirator_color  # type: str
        self.right_bottom_x = right_bottom_x  # type: str
        self.right_bottom_y = right_bottom_y  # type: str

    def validate(self):
        self.validate_required(self.feature, 'feature')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.image_base_six_four, 'image_base_six_four')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.local_feature, 'local_feature')
        self.validate_required(self.respirator_color, 'respirator_color')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')

    def to_map(self):
        result = {}
        result['Feature'] = self.feature
        result['FileName'] = self.file_name
        result['ImageBaseSixFour'] = self.image_base_six_four
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['LocalFeature'] = self.local_feature
        result['RespiratorColor'] = self.respirator_color
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        return result

    def from_map(self, map={}):
        self.feature = map.get('Feature')
        self.file_name = map.get('FileName')
        self.image_base_six_four = map.get('ImageBaseSixFour')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.local_feature = map.get('LocalFeature')
        self.respirator_color = map.get('RespiratorColor')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        return self


class RecognizeImageResponseDataFaceList(TeaModel):
    def __init__(self, feature=None, file_name=None, image_base_six_four=None, left_top_x=None, left_top_y=None,
                 local_feature=None, respirator_color=None, right_bottom_x=None, right_bottom_y=None, quality=None,
                 key_point_quality=None):
        self.feature = feature          # type: str
        self.file_name = file_name      # type: str
        self.image_base_six_four = image_base_six_four  # type: str
        self.left_top_x = left_top_x    # type: str
        self.left_top_y = left_top_y    # type: str
        self.local_feature = local_feature  # type: str
        self.respirator_color = respirator_color  # type: str
        self.right_bottom_x = right_bottom_x  # type: str
        self.right_bottom_y = right_bottom_y  # type: str
        self.quality = quality          # type: float
        self.key_point_quality = key_point_quality  # type: float

    def validate(self):
        self.validate_required(self.feature, 'feature')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.image_base_six_four, 'image_base_six_four')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.local_feature, 'local_feature')
        self.validate_required(self.respirator_color, 'respirator_color')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.quality, 'quality')
        self.validate_required(self.key_point_quality, 'key_point_quality')

    def to_map(self):
        result = {}
        result['Feature'] = self.feature
        result['FileName'] = self.file_name
        result['ImageBaseSixFour'] = self.image_base_six_four
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['LocalFeature'] = self.local_feature
        result['RespiratorColor'] = self.respirator_color
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['Quality'] = self.quality
        result['KeyPointQuality'] = self.key_point_quality
        return result

    def from_map(self, map={}):
        self.feature = map.get('Feature')
        self.file_name = map.get('FileName')
        self.image_base_six_four = map.get('ImageBaseSixFour')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.local_feature = map.get('LocalFeature')
        self.respirator_color = map.get('RespiratorColor')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.quality = map.get('Quality')
        self.key_point_quality = map.get('KeyPointQuality')
        return self


class RecognizeImageResponseData(TeaModel):
    def __init__(self, body_list=None, face_list=None):
        self.body_list = body_list      # type: List[RecognizeImageResponseDataBodyList]
        self.face_list = face_list      # type: List[RecognizeImageResponseDataFaceList]

    def validate(self):
        self.validate_required(self.body_list, 'body_list')
        if self.body_list:
            for k in self.body_list:
                if k:
                    k.validate()
        self.validate_required(self.face_list, 'face_list')
        if self.face_list:
            for k in self.face_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BodyList'] = []
        if self.body_list is not None:
            for k in self.body_list:
                result['BodyList'].append(k.to_map() if k else None)
        else:
            result['BodyList'] = None
        result['FaceList'] = []
        if self.face_list is not None:
            for k in self.face_list:
                result['FaceList'].append(k.to_map() if k else None)
        else:
            result['FaceList'] = None
        return result

    def from_map(self, map={}):
        self.body_list = []
        if map.get('BodyList') is not None:
            for k in map.get('BodyList'):
                temp_model = RecognizeImageResponseDataBodyList()
                self.body_list.append(temp_model.from_map(k))
        else:
            self.body_list = None
        self.face_list = []
        if map.get('FaceList') is not None:
            for k in map.get('FaceList'):
                temp_model = RecognizeImageResponseDataFaceList()
                self.face_list.append(temp_model.from_map(k))
        else:
            self.face_list = None
        return self


class ListCorpsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, corp_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.corp_name = corp_name      # type: str

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['CorpName'] = self.corp_name
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.corp_name = map.get('CorpName')
        return self


class ListCorpsResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListCorpsResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListCorpsResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListCorpsResponseDataRecords(TeaModel):
    def __init__(self, corp_id=None, corp_name=None, description=None, create_date=None, parent_corp_id=None,
                 app_name=None, device_count=None, isv_sub_id=None, acu_used=None, icon_path=None):
        self.corp_id = corp_id          # type: str
        self.corp_name = corp_name      # type: str
        self.description = description  # type: str
        self.create_date = create_date  # type: str
        self.parent_corp_id = parent_corp_id  # type: str
        self.app_name = app_name        # type: str
        self.device_count = device_count  # type: int
        self.isv_sub_id = isv_sub_id    # type: str
        self.acu_used = acu_used        # type: int
        self.icon_path = icon_path      # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.corp_name, 'corp_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.create_date, 'create_date')
        self.validate_required(self.parent_corp_id, 'parent_corp_id')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.device_count, 'device_count')
        self.validate_required(self.isv_sub_id, 'isv_sub_id')
        self.validate_required(self.acu_used, 'acu_used')
        self.validate_required(self.icon_path, 'icon_path')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['CorpName'] = self.corp_name
        result['Description'] = self.description
        result['CreateDate'] = self.create_date
        result['ParentCorpId'] = self.parent_corp_id
        result['AppName'] = self.app_name
        result['DeviceCount'] = self.device_count
        result['IsvSubId'] = self.isv_sub_id
        result['AcuUsed'] = self.acu_used
        result['IconPath'] = self.icon_path
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.corp_name = map.get('CorpName')
        self.description = map.get('Description')
        self.create_date = map.get('CreateDate')
        self.parent_corp_id = map.get('ParentCorpId')
        self.app_name = map.get('AppName')
        self.device_count = map.get('DeviceCount')
        self.isv_sub_id = map.get('IsvSubId')
        self.acu_used = map.get('AcuUsed')
        self.icon_path = map.get('IconPath')
        return self


class ListCorpsResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[ListCorpsResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListCorpsResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class UpdateCorpRequest(TeaModel):
    def __init__(self, corp_id=None, corp_name=None, app_name=None, parent_corp_id=None, description=None,
                 isv_sub_id=None, icon_path=None):
        self.corp_id = corp_id          # type: str
        self.corp_name = corp_name      # type: str
        self.app_name = app_name        # type: str
        self.parent_corp_id = parent_corp_id  # type: str
        self.description = description  # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.icon_path = icon_path      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['CorpName'] = self.corp_name
        result['AppName'] = self.app_name
        result['ParentCorpId'] = self.parent_corp_id
        result['Description'] = self.description
        result['IsvSubId'] = self.isv_sub_id
        result['IconPath'] = self.icon_path
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.corp_name = map.get('CorpName')
        self.app_name = map.get('AppName')
        self.parent_corp_id = map.get('ParentCorpId')
        self.description = map.get('Description')
        self.isv_sub_id = map.get('IsvSubId')
        self.icon_path = map.get('IconPath')
        return self


class UpdateCorpResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class UpdateDeviceRequest(TeaModel):
    def __init__(self, gb_id=None, device_name=None, device_type=None, device_address=None, device_site=None,
                 device_direction=None, device_resolution=None, bit_rate=None, corp_id=None, vendor=None):
        self.gb_id = gb_id              # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: str
        self.device_address = device_address  # type: str
        self.device_site = device_site  # type: str
        self.device_direction = device_direction  # type: str
        self.device_resolution = device_resolution  # type: str
        self.bit_rate = bit_rate        # type: str
        self.corp_id = corp_id          # type: str
        self.vendor = vendor            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['GbId'] = self.gb_id
        result['DeviceName'] = self.device_name
        result['DeviceType'] = self.device_type
        result['DeviceAddress'] = self.device_address
        result['DeviceSite'] = self.device_site
        result['DeviceDirection'] = self.device_direction
        result['DeviceResolution'] = self.device_resolution
        result['BitRate'] = self.bit_rate
        result['CorpId'] = self.corp_id
        result['Vendor'] = self.vendor
        return result

    def from_map(self, map={}):
        self.gb_id = map.get('GbId')
        self.device_name = map.get('DeviceName')
        self.device_type = map.get('DeviceType')
        self.device_address = map.get('DeviceAddress')
        self.device_site = map.get('DeviceSite')
        self.device_direction = map.get('DeviceDirection')
        self.device_resolution = map.get('DeviceResolution')
        self.bit_rate = map.get('BitRate')
        self.corp_id = map.get('CorpId')
        self.vendor = map.get('Vendor')
        return self


class UpdateDeviceResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class ListDevicesRequest(TeaModel):
    def __init__(self, corp_id=None, gb_id=None, device_name=None, page_number=None, page_size=None):
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str
        self.device_name = device_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        result['DeviceName'] = self.device_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        self.device_name = map.get('DeviceName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class ListDevicesResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: ListDevicesResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ListDevicesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListDevicesResponseDataRecords(TeaModel):
    def __init__(self, access_protocol_type=None, bit_rate=None, cover_image_url=None, gb_id=None,
                 device_address=None, device_direction=None, device_site=None, latitude=None, longitude=None, device_name=None,
                 resolution=None, sip_gbid=None, sip_password=None, sip_server_ip=None, sip_server_port=None, status=None,
                 device_type=None, vendor=None, create_time=None):
        self.access_protocol_type = access_protocol_type  # type: str
        self.bit_rate = bit_rate        # type: str
        self.cover_image_url = cover_image_url  # type: str
        self.gb_id = gb_id              # type: str
        self.device_address = device_address  # type: str
        self.device_direction = device_direction  # type: str
        self.device_site = device_site  # type: str
        self.latitude = latitude        # type: str
        self.longitude = longitude      # type: str
        self.device_name = device_name  # type: str
        self.resolution = resolution    # type: str
        self.sip_gbid = sip_gbid        # type: str
        self.sip_password = sip_password  # type: str
        self.sip_server_ip = sip_server_ip  # type: str
        self.sip_server_port = sip_server_port  # type: str
        self.status = status            # type: int
        self.device_type = device_type  # type: str
        self.vendor = vendor            # type: str
        self.create_time = create_time  # type: str

    def validate(self):
        self.validate_required(self.access_protocol_type, 'access_protocol_type')
        self.validate_required(self.bit_rate, 'bit_rate')
        self.validate_required(self.cover_image_url, 'cover_image_url')
        self.validate_required(self.gb_id, 'gb_id')
        self.validate_required(self.device_address, 'device_address')
        self.validate_required(self.device_direction, 'device_direction')
        self.validate_required(self.device_site, 'device_site')
        self.validate_required(self.latitude, 'latitude')
        self.validate_required(self.longitude, 'longitude')
        self.validate_required(self.device_name, 'device_name')
        self.validate_required(self.resolution, 'resolution')
        self.validate_required(self.sip_gbid, 'sip_gbid')
        self.validate_required(self.sip_password, 'sip_password')
        self.validate_required(self.sip_server_ip, 'sip_server_ip')
        self.validate_required(self.sip_server_port, 'sip_server_port')
        self.validate_required(self.status, 'status')
        self.validate_required(self.device_type, 'device_type')
        self.validate_required(self.vendor, 'vendor')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['AccessProtocolType'] = self.access_protocol_type
        result['BitRate'] = self.bit_rate
        result['CoverImageUrl'] = self.cover_image_url
        result['GbId'] = self.gb_id
        result['DeviceAddress'] = self.device_address
        result['DeviceDirection'] = self.device_direction
        result['DeviceSite'] = self.device_site
        result['Latitude'] = self.latitude
        result['Longitude'] = self.longitude
        result['DeviceName'] = self.device_name
        result['Resolution'] = self.resolution
        result['SipGBId'] = self.sip_gbid
        result['SipPassword'] = self.sip_password
        result['SipServerIp'] = self.sip_server_ip
        result['SipServerPort'] = self.sip_server_port
        result['Status'] = self.status
        result['DeviceType'] = self.device_type
        result['Vendor'] = self.vendor
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.access_protocol_type = map.get('AccessProtocolType')
        self.bit_rate = map.get('BitRate')
        self.cover_image_url = map.get('CoverImageUrl')
        self.gb_id = map.get('GbId')
        self.device_address = map.get('DeviceAddress')
        self.device_direction = map.get('DeviceDirection')
        self.device_site = map.get('DeviceSite')
        self.latitude = map.get('Latitude')
        self.longitude = map.get('Longitude')
        self.device_name = map.get('DeviceName')
        self.resolution = map.get('Resolution')
        self.sip_gbid = map.get('SipGBId')
        self.sip_password = map.get('SipPassword')
        self.sip_server_ip = map.get('SipServerIp')
        self.sip_server_port = map.get('SipServerPort')
        self.status = map.get('Status')
        self.device_type = map.get('DeviceType')
        self.vendor = map.get('Vendor')
        self.create_time = map.get('CreateTime')
        return self


class ListDevicesResponseData(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[ListDevicesResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = ListDevicesResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class GetDeviceLiveUrlRequest(TeaModel):
    def __init__(self, device_id=None, stream_type=None, out_protocol=None, corp_id=None, gb_id=None):
        self.device_id = device_id      # type: str
        self.stream_type = stream_type  # type: int
        self.out_protocol = out_protocol  # type: str
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DeviceId'] = self.device_id
        result['StreamType'] = self.stream_type
        result['OutProtocol'] = self.out_protocol
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        return result

    def from_map(self, map={}):
        self.device_id = map.get('DeviceId')
        self.stream_type = map.get('StreamType')
        self.out_protocol = map.get('OutProtocol')
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        return self


class GetDeviceLiveUrlResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, url=None, out_protocol=None, stream_type=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.url = url                  # type: str
        self.out_protocol = out_protocol  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.url, 'url')
        self.validate_required(self.out_protocol, 'out_protocol')
        self.validate_required(self.stream_type, 'stream_type')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Url'] = self.url
        result['OutProtocol'] = self.out_protocol
        result['StreamType'] = self.stream_type
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.url = map.get('Url')
        self.out_protocol = map.get('OutProtocol')
        self.stream_type = map.get('StreamType')
        return self


class SearchFaceRequest(TeaModel):
    def __init__(self, corp_id=None, gb_id=None, start_time_stamp=None, end_time_stamp=None, page_no=None,
                 page_size=None, option_list=None):
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str
        self.start_time_stamp = start_time_stamp  # type: int
        self.end_time_stamp = end_time_stamp  # type: int
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.option_list = option_list  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.start_time_stamp, 'start_time_stamp')
        self.validate_required(self.end_time_stamp, 'end_time_stamp')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        result['StartTimeStamp'] = self.start_time_stamp
        result['EndTimeStamp'] = self.end_time_stamp
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['OptionList'] = self.option_list
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        self.start_time_stamp = map.get('StartTimeStamp')
        self.end_time_stamp = map.get('EndTimeStamp')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.option_list = map.get('OptionList')
        return self


class SearchFaceShrinkRequest(TeaModel):
    def __init__(self, corp_id=None, gb_id=None, start_time_stamp=None, end_time_stamp=None, page_no=None,
                 page_size=None, option_list_shrink=None):
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str
        self.start_time_stamp = start_time_stamp  # type: int
        self.end_time_stamp = end_time_stamp  # type: int
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.option_list_shrink = option_list_shrink  # type: str

    def validate(self):
        self.validate_required(self.corp_id, 'corp_id')
        self.validate_required(self.start_time_stamp, 'start_time_stamp')
        self.validate_required(self.end_time_stamp, 'end_time_stamp')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        result['StartTimeStamp'] = self.start_time_stamp
        result['EndTimeStamp'] = self.end_time_stamp
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['OptionList'] = self.option_list_shrink
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        self.start_time_stamp = map.get('StartTimeStamp')
        self.end_time_stamp = map.get('EndTimeStamp')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.option_list_shrink = map.get('OptionList')
        return self


class SearchFaceResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: SearchFaceResponseData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SearchFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class SearchFaceResponseDataRecords(TeaModel):
    def __init__(self, gb_id=None, image_url=None, left_top_x=None, left_top_y=None, match_suggestion=None,
                 right_bottom_x=None, right_bottom_y=None, score=None, target_image_url=None, source_id=None):
        self.gb_id = gb_id              # type: str
        self.image_url = image_url      # type: str
        self.left_top_x = left_top_x    # type: float
        self.left_top_y = left_top_y    # type: float
        self.match_suggestion = match_suggestion  # type: str
        self.right_bottom_x = right_bottom_x  # type: float
        self.right_bottom_y = right_bottom_y  # type: float
        self.score = score              # type: float
        self.target_image_url = target_image_url  # type: str
        self.source_id = source_id      # type: str

    def validate(self):
        self.validate_required(self.gb_id, 'gb_id')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.left_top_x, 'left_top_x')
        self.validate_required(self.left_top_y, 'left_top_y')
        self.validate_required(self.match_suggestion, 'match_suggestion')
        self.validate_required(self.right_bottom_x, 'right_bottom_x')
        self.validate_required(self.right_bottom_y, 'right_bottom_y')
        self.validate_required(self.score, 'score')
        self.validate_required(self.target_image_url, 'target_image_url')
        self.validate_required(self.source_id, 'source_id')

    def to_map(self):
        result = {}
        result['GbId'] = self.gb_id
        result['ImageUrl'] = self.image_url
        result['LeftTopX'] = self.left_top_x
        result['LeftTopY'] = self.left_top_y
        result['MatchSuggestion'] = self.match_suggestion
        result['RightBottomX'] = self.right_bottom_x
        result['RightBottomY'] = self.right_bottom_y
        result['Score'] = self.score
        result['TargetImageUrl'] = self.target_image_url
        result['SourceId'] = self.source_id
        return result

    def from_map(self, map={}):
        self.gb_id = map.get('GbId')
        self.image_url = map.get('ImageUrl')
        self.left_top_x = map.get('LeftTopX')
        self.left_top_y = map.get('LeftTopY')
        self.match_suggestion = map.get('MatchSuggestion')
        self.right_bottom_x = map.get('RightBottomX')
        self.right_bottom_y = map.get('RightBottomY')
        self.score = map.get('Score')
        self.target_image_url = map.get('TargetImageUrl')
        self.source_id = map.get('SourceId')
        return self


class SearchFaceResponseData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total_count=None, total_page=None, records=None):
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page    # type: int
        self.records = records          # type: List[SearchFaceResponseDataRecords]

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TotalPage'] = self.total_page
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.total_page = map.get('TotalPage')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = SearchFaceResponseDataRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class AddDeviceRequest(TeaModel):
    def __init__(self, gb_id=None, device_name=None, device_type=None, device_address=None, device_site=None,
                 device_direction=None, device_resolution=None, bit_rate=None, corp_id=None, vendor=None):
        self.gb_id = gb_id              # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: str
        self.device_address = device_address  # type: str
        self.device_site = device_site  # type: str
        self.device_direction = device_direction  # type: str
        self.device_resolution = device_resolution  # type: str
        self.bit_rate = bit_rate        # type: str
        self.corp_id = corp_id          # type: str
        self.vendor = vendor            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['GbId'] = self.gb_id
        result['DeviceName'] = self.device_name
        result['DeviceType'] = self.device_type
        result['DeviceAddress'] = self.device_address
        result['DeviceSite'] = self.device_site
        result['DeviceDirection'] = self.device_direction
        result['DeviceResolution'] = self.device_resolution
        result['BitRate'] = self.bit_rate
        result['CorpId'] = self.corp_id
        result['Vendor'] = self.vendor
        return result

    def from_map(self, map={}):
        self.gb_id = map.get('GbId')
        self.device_name = map.get('DeviceName')
        self.device_type = map.get('DeviceType')
        self.device_address = map.get('DeviceAddress')
        self.device_site = map.get('DeviceSite')
        self.device_direction = map.get('DeviceDirection')
        self.device_resolution = map.get('DeviceResolution')
        self.bit_rate = map.get('BitRate')
        self.corp_id = map.get('CorpId')
        self.vendor = map.get('Vendor')
        return self


class AddDeviceResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class CreateCorpRequest(TeaModel):
    def __init__(self, corp_name=None, app_name=None, parent_corp_id=None, description=None, algorithm_type=None,
                 isv_sub_id=None, icon_path=None):
        self.corp_name = corp_name      # type: str
        self.app_name = app_name        # type: str
        self.parent_corp_id = parent_corp_id  # type: str
        self.description = description  # type: str
        self.algorithm_type = algorithm_type  # type: str
        self.isv_sub_id = isv_sub_id    # type: str
        self.icon_path = icon_path      # type: str

    def validate(self):
        self.validate_required(self.corp_name, 'corp_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['CorpName'] = self.corp_name
        result['AppName'] = self.app_name
        result['ParentCorpId'] = self.parent_corp_id
        result['Description'] = self.description
        result['AlgorithmType'] = self.algorithm_type
        result['IsvSubId'] = self.isv_sub_id
        result['IconPath'] = self.icon_path
        return result

    def from_map(self, map={}):
        self.corp_name = map.get('CorpName')
        self.app_name = map.get('AppName')
        self.parent_corp_id = map.get('ParentCorpId')
        self.description = map.get('Description')
        self.algorithm_type = map.get('AlgorithmType')
        self.isv_sub_id = map.get('IsvSubId')
        self.icon_path = map.get('IconPath')
        return self


class CreateCorpResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, corp_id=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.corp_id = corp_id          # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.corp_id, 'corp_id')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['CorpId'] = self.corp_id
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.corp_id = map.get('CorpId')
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(self, corp_id=None, gb_id=None):
        self.corp_id = corp_id          # type: str
        self.gb_id = gb_id              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CorpId'] = self.corp_id
        result['GbId'] = self.gb_id
        return result

    def from_map(self, map={}):
        self.corp_id = map.get('CorpId')
        self.gb_id = map.get('GbId')
        return self


class DeleteDeviceResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data=None, message=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.data = data                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Data'] = self.data
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.data = map.get('Data')
        self.message = map.get('Message')
        return self
