# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MLDataSetParam(DaraModel):
    def __init__(
        self,
        create_by: str = None,
        create_time: int = None,
        data_type: str = None,
        dataset_id: str = None,
        description: str = None,
        label_id: str = None,
        last_modify_time: int = None,
        name: str = None,
        setting_type: str = None,
    ):
        self.create_by = create_by
        self.create_time = create_time
        self.data_type = data_type
        self.dataset_id = dataset_id
        self.description = description
        self.label_id = label_id
        self.last_modify_time = last_modify_time
        self.name = name
        self.setting_type = setting_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_by is not None:
            result['createBy'] = self.create_by

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.description is not None:
            result['description'] = self.description

        if self.label_id is not None:
            result['labelId'] = self.label_id

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.name is not None:
            result['name'] = self.name

        if self.setting_type is not None:
            result['settingType'] = self.setting_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createBy') is not None:
            self.create_by = m.get('createBy')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('labelId') is not None:
            self.label_id = m.get('labelId')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('settingType') is not None:
            self.setting_type = m.get('settingType')

        return self

