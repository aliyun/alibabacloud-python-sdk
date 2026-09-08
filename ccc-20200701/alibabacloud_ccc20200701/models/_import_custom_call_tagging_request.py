# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportCustomCallTaggingRequest(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        instance_id: str = None,
    ):
        # The ObjectKey of the OSS object that contains the inbound number mark file. OSS is configured with the public customer storage bucket for Cloud Call Center. You can upload the inbound number mark file to this public customer storage bucket through the inbound management page of Cloud Call Center. After the upload succeeds, invoking this API reads the file content from OSS and imports it in batch. We do not recommend directly invoking this API. Instead, you can perform this operation through the default public cloud CRM System provided by Cloud Call Center.
        # 
        # This parameter is required.
        self.file_path = file_path
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

