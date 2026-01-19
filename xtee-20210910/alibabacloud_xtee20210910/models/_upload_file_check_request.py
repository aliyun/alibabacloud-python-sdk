# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadFileCheckRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        batch_name: str = None,
        data_type: str = None,
        oss_file_name: str = None,
        reg_id: str = None,
        sample_tag_type: str = None,
        service_list: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Sample batch name
        self.batch_name = batch_name
        # Data type
        self.data_type = data_type
        # Uploaded OSS address.
        self.oss_file_name = oss_file_name
        # Region code
        self.reg_id = reg_id
        # Sample type
        self.sample_tag_type = sample_tag_type
        # Service list
        self.service_list = service_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.batch_name is not None:
            result['batchName'] = self.batch_name

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.oss_file_name is not None:
            result['ossFileName'] = self.oss_file_name

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_tag_type is not None:
            result['sampleTagType'] = self.sample_tag_type

        if self.service_list is not None:
            result['serviceList'] = self.service_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('batchName') is not None:
            self.batch_name = m.get('batchName')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('ossFileName') is not None:
            self.oss_file_name = m.get('ossFileName')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleTagType') is not None:
            self.sample_tag_type = m.get('sampleTagType')

        if m.get('serviceList') is not None:
            self.service_list = m.get('serviceList')

        return self

