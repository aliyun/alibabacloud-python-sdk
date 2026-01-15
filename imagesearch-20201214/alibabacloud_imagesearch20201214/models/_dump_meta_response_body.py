# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imagesearch20201214 import models as main_models
from darabonba.model import DaraModel

class DumpMetaResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DumpMetaResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the export task.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DumpMetaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DumpMetaResponseBodyData(DaraModel):
    def __init__(
        self,
        dump_meta_status: str = None,
        id: str = None,
    ):
        # The status of the export task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.dump_meta_status = dump_meta_status
        # The ID of the export task.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dump_meta_status is not None:
            result['DumpMetaStatus'] = self.dump_meta_status

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DumpMetaStatus') is not None:
            self.dump_meta_status = m.get('DumpMetaStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

