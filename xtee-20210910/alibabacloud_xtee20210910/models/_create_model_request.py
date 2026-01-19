# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelRequest(DaraModel):
    def __init__(
        self,
        buc_id: str = None,
        counts: str = None,
        file_md5: str = None,
        file_path: str = None,
        model_name: str = None,
        model_scene: str = None,
        parameter_num: str = None,
        reg_id: str = None,
        user_local_file_name: str = None,
    ):
        # Submitter ID.
        # 
        # This parameter is required.
        self.buc_id = buc_id
        # Number of file rows.
        # 
        # This parameter is required.
        self.counts = counts
        # File MD5 value.
        # 
        # This parameter is required.
        self.file_md5 = file_md5
        # File path.
        # 
        # This parameter is required.
        self.file_path = file_path
        # Model name.
        # 
        # This parameter is required.
        self.model_name = model_name
        # Model scenario.
        # 
        # This parameter is required.
        self.model_scene = model_scene
        # Number of file columns.
        # 
        # This parameter is required.
        self.parameter_num = parameter_num
        # Region code
        self.reg_id = reg_id
        # Uploaded file name.
        # 
        # This parameter is required.
        self.user_local_file_name = user_local_file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buc_id is not None:
            result['BucId'] = self.buc_id

        if self.counts is not None:
            result['Counts'] = self.counts

        if self.file_md5 is not None:
            result['FileMD5'] = self.file_md5

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_scene is not None:
            result['ModelScene'] = self.model_scene

        if self.parameter_num is not None:
            result['ParameterNum'] = self.parameter_num

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.user_local_file_name is not None:
            result['UserLocalFileName'] = self.user_local_file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucId') is not None:
            self.buc_id = m.get('BucId')

        if m.get('Counts') is not None:
            self.counts = m.get('Counts')

        if m.get('FileMD5') is not None:
            self.file_md5 = m.get('FileMD5')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelScene') is not None:
            self.model_scene = m.get('ModelScene')

        if m.get('ParameterNum') is not None:
            self.parameter_num = m.get('ParameterNum')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('UserLocalFileName') is not None:
            self.user_local_file_name = m.get('UserLocalFileName')

        return self

