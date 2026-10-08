# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class QuerySlsLogStoreListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.QuerySlsLogStoreListResponseBodyResult] = None,
        total_size: int = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The configurations of Log Service for the application.
        self.result = result
        # The number of log sources configured for the application.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QuerySlsLogStoreListResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class QuerySlsLogStoreListResponseBodyResult(DaraModel):
    def __init__(
        self,
        consumer_side: str = None,
        create_time: str = None,
        link: str = None,
        logstore: str = None,
        project: str = None,
        source: str = None,
    ):
        # The type of the logging service.
        self.consumer_side = consumer_side
        # The time when the logging service was created.
        self.create_time = create_time
        # The URL of the logging service.
        self.link = link
        # The name of the Logstore.
        self.logstore = logstore
        # The name of the project.
        self.project = project
        # The source of logs. Valid values:
        # 
        # - Standard output: stdout.log
        # 
        # - File log: the directory that stores logs
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_side is not None:
            result['ConsumerSide'] = self.consumer_side

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.link is not None:
            result['Link'] = self.link

        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerSide') is not None:
            self.consumer_side = m.get('ConsumerSide')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

