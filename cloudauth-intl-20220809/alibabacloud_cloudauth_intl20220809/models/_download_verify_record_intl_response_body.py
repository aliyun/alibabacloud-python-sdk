# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class DownloadVerifyRecordIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DownloadVerifyRecordIntlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Return code.
        self.code = code
        # Returned data.
        self.data = data
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DownloadVerifyRecordIntlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DownloadVerifyRecordIntlResponseBodyData(DaraModel):
    def __init__(
        self,
        download_task_id: str = None,
        url: str = None,
    ):
        # Task ID, returned in asynchronous mode, used later with QueryDownloadTaskIntl to download the exported file.
        self.download_task_id = download_task_id
        # Exported file download link.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_task_id is not None:
            result['DownloadTaskId'] = self.download_task_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadTaskId') is not None:
            self.download_task_id = m.get('DownloadTaskId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

