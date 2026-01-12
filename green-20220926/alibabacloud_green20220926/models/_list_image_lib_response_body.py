# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListImageLibResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        lib_list: List[main_models.ListImageLibResponseBodyLibList] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error code, consistent with HTTP status.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # List of image library information.
        self.lib_list = lib_list
        # Further description of the error code.
        self.msg = msg
        # ID assigned by the backend to uniquely identify a request. Can be used for troubleshooting.
        self.request_id = request_id
        # Success indicator.
        self.success = success

    def validate(self):
        if self.lib_list:
            for v1 in self.lib_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['LibList'] = []
        if self.lib_list is not None:
            for k1 in self.lib_list:
                result['LibList'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.lib_list = []
        if m.get('LibList') is not None:
            for k1 in m.get('LibList'):
                temp_model = main_models.ListImageLibResponseBodyLibList()
                self.lib_list.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListImageLibResponseBodyLibList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        free_inspection: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_num: int = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # Comment.
        self.comment = comment
        # Exempt from inspection configuration.
        self.free_inspection = free_inspection
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time.
        self.gmt_modified = gmt_modified
        # Number of images in the library.
        self.image_num = image_num
        # Library ID.
        self.lib_id = lib_id
        # Library name.
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.free_inspection is not None:
            result['FreeInspection'] = self.free_inspection

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_num is not None:
            result['ImageNum'] = self.image_num

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('FreeInspection') is not None:
            self.free_inspection = m.get('FreeInspection')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageNum') is not None:
            self.image_num = m.get('ImageNum')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        return self

