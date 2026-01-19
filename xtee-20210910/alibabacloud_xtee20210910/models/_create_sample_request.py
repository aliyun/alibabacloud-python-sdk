# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSampleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        client_file_name: str = None,
        client_path: str = None,
        file_type: str = None,
        reg_id: str = None,
        sample_tag: str = None,
        sample_type: str = None,
        sample_values: str = None,
        upload_type: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # OSS client uploaded file name
        self.client_file_name = client_file_name
        # OSS client address
        self.client_path = client_path
        # File type
        self.file_type = file_type
        # Region code
        self.reg_id = reg_id
        # Sample tag
        self.sample_tag = sample_tag
        # Sample type
        self.sample_type = sample_type
        # Sample values
        self.sample_values = sample_values
        # Upload type
        self.upload_type = upload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.client_file_name is not None:
            result['clientFileName'] = self.client_file_name

        if self.client_path is not None:
            result['clientPath'] = self.client_path

        if self.file_type is not None:
            result['fileType'] = self.file_type

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.sample_tag is not None:
            result['sampleTag'] = self.sample_tag

        if self.sample_type is not None:
            result['sampleType'] = self.sample_type

        if self.sample_values is not None:
            result['sampleValues'] = self.sample_values

        if self.upload_type is not None:
            result['uploadType'] = self.upload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('clientFileName') is not None:
            self.client_file_name = m.get('clientFileName')

        if m.get('clientPath') is not None:
            self.client_path = m.get('clientPath')

        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('sampleTag') is not None:
            self.sample_tag = m.get('sampleTag')

        if m.get('sampleType') is not None:
            self.sample_type = m.get('sampleType')

        if m.get('sampleValues') is not None:
            self.sample_values = m.get('sampleValues')

        if m.get('uploadType') is not None:
            self.upload_type = m.get('uploadType')

        return self

