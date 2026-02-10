# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class BatchCreateMaliciousNoteRequest(DaraModel):
    def __init__(
        self,
        image_malicious_file_list: List[main_models.BatchCreateMaliciousNoteRequestImageMaliciousFileList] = None,
    ):
        # The batches.
        self.image_malicious_file_list = image_malicious_file_list

    def validate(self):
        if self.image_malicious_file_list:
            for v1 in self.image_malicious_file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageMaliciousFileList'] = []
        if self.image_malicious_file_list is not None:
            for k1 in self.image_malicious_file_list:
                result['ImageMaliciousFileList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_malicious_file_list = []
        if m.get('ImageMaliciousFileList') is not None:
            for k1 in m.get('ImageMaliciousFileList'):
                temp_model = main_models.BatchCreateMaliciousNoteRequestImageMaliciousFileList()
                self.image_malicious_file_list.append(temp_model.from_map(k1))

        return self

class BatchCreateMaliciousNoteRequestImageMaliciousFileList(DaraModel):
    def __init__(
        self,
        event_id: int = None,
        note: str = None,
    ):
        # The ID of the alert.
        # 
        # >  You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to query the alert IDs.
        self.event_id = event_id
        # The description.
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.note is not None:
            result['Note'] = self.note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        return self

