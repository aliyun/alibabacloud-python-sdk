# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddUnknownThreatDetectProcessRequest(DaraModel):
    def __init__(
        self,
        event_id_list: List[int] = None,
        process_list: List[main_models.AddUnknownThreatDetectProcessRequestProcessList] = None,
        uuid_list: List[str] = None,
    ):
        # A list of associated event IDs.
        self.event_id_list = event_id_list
        # The list of processes to add.
        self.process_list = process_list
        # The UUIDs of assets on which the processes are located.
        self.uuid_list = uuid_list

    def validate(self):
        if self.process_list:
            for v1 in self.process_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id_list is not None:
            result['EventIdList'] = self.event_id_list

        result['ProcessList'] = []
        if self.process_list is not None:
            for k1 in self.process_list:
                result['ProcessList'].append(k1.to_map() if k1 else None)

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventIdList') is not None:
            self.event_id_list = m.get('EventIdList')

        self.process_list = []
        if m.get('ProcessList') is not None:
            for k1 in m.get('ProcessList'):
                temp_model = main_models.AddUnknownThreatDetectProcessRequestProcessList()
                self.process_list.append(temp_model.from_map(k1))

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

class AddUnknownThreatDetectProcessRequestProcessList(DaraModel):
    def __init__(
        self,
        md_5: str = None,
        process_path: str = None,
        remark: str = None,
        sha_256: str = None,
    ):
        # The MD5 hash of the process file.
        self.md_5 = md_5
        # The path to the process executable.
        self.process_path = process_path
        # A remark for the process.
        self.remark = remark
        # The SHA-256 hash of the process file.
        self.sha_256 = sha_256

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sha_256 is not None:
            result['Sha256'] = self.sha_256

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Sha256') is not None:
            self.sha_256 = m.get('Sha256')

        return self

