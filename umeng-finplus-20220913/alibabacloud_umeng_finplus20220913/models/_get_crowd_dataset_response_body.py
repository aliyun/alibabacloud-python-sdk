# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class GetCrowdDatasetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCrowdDatasetResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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

        if m.get('Data') is not None:
            temp_model = main_models.GetCrowdDatasetResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCrowdDatasetResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        crowd_dataset_id: str = None,
        dataset_ids: str = None,
        description: str = None,
        name: str = None,
        upload_status: str = None,
    ):
        self.app_id = app_id
        self.crowd_dataset_id = crowd_dataset_id
        self.dataset_ids = dataset_ids
        self.description = description
        self.name = name
        self.upload_status = upload_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.crowd_dataset_id is not None:
            result['crowdDatasetId'] = self.crowd_dataset_id

        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.upload_status is not None:
            result['uploadStatus'] = self.upload_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('crowdDatasetId') is not None:
            self.crowd_dataset_id = m.get('crowdDatasetId')

        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('uploadStatus') is not None:
            self.upload_status = m.get('uploadStatus')

        return self

