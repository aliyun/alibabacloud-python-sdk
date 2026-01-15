# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class DumpMetaListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DumpMetaListResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the task that is used to export metadata.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DumpMetaListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DumpMetaListResponseBodyData(DaraModel):
    def __init__(
        self,
        dump_meta_list: List[main_models.DumpMetaListResponseBodyDataDumpMetaList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # A list of tasks that are used to export metadata.
        self.dump_meta_list = dump_meta_list
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.dump_meta_list:
            for v1 in self.dump_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DumpMetaList'] = []
        if self.dump_meta_list is not None:
            for k1 in self.dump_meta_list:
                result['DumpMetaList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dump_meta_list = []
        if m.get('DumpMetaList') is not None:
            for k1 in m.get('DumpMetaList'):
                temp_model = main_models.DumpMetaListResponseBodyDataDumpMetaList()
                self.dump_meta_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DumpMetaListResponseBodyDataDumpMetaList(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        meta_url: str = None,
        msg: str = None,
        status: str = None,
        utc_create: str = None,
        utc_modified: int = None,
    ):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The ID of the task.
        self.id = id
        # The address where you can download the metadata. The address is valid for 2 hours.
        self.meta_url = meta_url
        # The error message returned.
        self.msg = msg
        # The status of the export task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.status = status
        # The time when the task was created. Unit: milliseconds.
        self.utc_create = utc_create
        # The time when the task was updated. Unit: milliseconds.
        self.utc_modified = utc_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.status is not None:
            result['Status'] = self.status

        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create

        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')

        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')

        return self

