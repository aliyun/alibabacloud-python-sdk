# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        directory: main_models.GetDirectoryResponseBodyDirectory = None,
        request_id: str = None,
    ):
        # The information about the directory.
        self.directory = directory
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.directory:
            self.directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory is not None:
            result['Directory'] = self.directory.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            temp_model = main_models.GetDirectoryResponseBodyDirectory()
            self.directory = temp_model.from_map(m.get('Directory'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDirectoryResponseBodyDirectory(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        directory_name: str = None,
        region: str = None,
        update_time: str = None,
    ):
        # The time when the directory was created.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the directory.
        self.directory_name = directory_name
        # The region ID of the directory.
        self.region = region
        # The time when the directory was modified.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        if self.region is not None:
            result['Region'] = self.region

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

