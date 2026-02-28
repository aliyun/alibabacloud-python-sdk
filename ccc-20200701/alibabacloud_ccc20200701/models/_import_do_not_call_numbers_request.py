# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportDoNotCallNumbersRequest(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        instance_id: str = None,
        number_list: str = None,
        remark: str = None,
    ):
        self.file_path = file_path
        # This parameter is required.
        self.instance_id = instance_id
        self.number_list = number_list
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

