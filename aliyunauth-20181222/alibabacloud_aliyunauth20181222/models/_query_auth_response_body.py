# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliyunauth20181222 import models as main_models
from darabonba.model import DaraModel

class QueryAuthResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryAuthResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAuthResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAuthResponseBodyData(DaraModel):
    def __init__(
        self,
        info_dtolist: main_models.QueryAuthResponseBodyDataInfoDTOList = None,
        instance_id: str = None,
        product_code: str = None,
    ):
        self.info_dtolist = info_dtolist
        self.instance_id = instance_id
        self.product_code = product_code

    def validate(self):
        if self.info_dtolist:
            self.info_dtolist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_dtolist is not None:
            result['InfoDTOList'] = self.info_dtolist.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoDTOList') is not None:
            temp_model = main_models.QueryAuthResponseBodyDataInfoDTOList()
            self.info_dtolist = temp_model.from_map(m.get('InfoDTOList'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

class QueryAuthResponseBodyDataInfoDTOList(DaraModel):
    def __init__(
        self,
        info_dtolist: List[main_models.QueryAuthResponseBodyDataInfoDTOListInfoDTOList] = None,
    ):
        self.info_dtolist = info_dtolist

    def validate(self):
        if self.info_dtolist:
            for v1 in self.info_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InfoDTOList'] = []
        if self.info_dtolist is not None:
            for k1 in self.info_dtolist:
                result['InfoDTOList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info_dtolist = []
        if m.get('InfoDTOList') is not None:
            for k1 in m.get('InfoDTOList'):
                temp_model = main_models.QueryAuthResponseBodyDataInfoDTOListInfoDTOList()
                self.info_dtolist.append(temp_model.from_map(k1))

        return self

class QueryAuthResponseBodyDataInfoDTOListInfoDTOList(DaraModel):
    def __init__(
        self,
        auth_order_vid: str = None,
        item_name: str = None,
        item_record_vid: str = None,
        operate_code: str = None,
    ):
        self.auth_order_vid = auth_order_vid
        self.item_name = item_name
        self.item_record_vid = item_record_vid
        self.operate_code = operate_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_order_vid is not None:
            result['AuthOrderVid'] = self.auth_order_vid

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.item_record_vid is not None:
            result['ItemRecordVid'] = self.item_record_vid

        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthOrderVid') is not None:
            self.auth_order_vid = m.get('AuthOrderVid')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('ItemRecordVid') is not None:
            self.item_record_vid = m.get('ItemRecordVid')

        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')

        return self

