# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class GetYzdInstanceTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: bool = None,
        data: List[main_models.GetYzdInstanceTaskResultResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetYzdInstanceTaskResultResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetYzdInstanceTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        appid: str = None,
        bcid: str = None,
        dataset_ids: str = None,
        download_urls: List[main_models.GetYzdInstanceTaskResultResponseBodyDataDownloadUrls] = None,
        result_cnt: str = None,
        status: str = None,
        time_duration: str = None,
    ):
        self.appid = appid
        self.bcid = bcid
        self.dataset_ids = dataset_ids
        self.download_urls = download_urls
        self.result_cnt = result_cnt
        self.status = status
        self.time_duration = time_duration

    def validate(self):
        if self.download_urls:
            for v1 in self.download_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appid is not None:
            result['appid'] = self.appid

        if self.bcid is not None:
            result['bcid'] = self.bcid

        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids

        result['downloadUrls'] = []
        if self.download_urls is not None:
            for k1 in self.download_urls:
                result['downloadUrls'].append(k1.to_map() if k1 else None)

        if self.result_cnt is not None:
            result['resultCnt'] = self.result_cnt

        if self.status is not None:
            result['status'] = self.status

        if self.time_duration is not None:
            result['timeDuration'] = self.time_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appid') is not None:
            self.appid = m.get('appid')

        if m.get('bcid') is not None:
            self.bcid = m.get('bcid')

        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')

        self.download_urls = []
        if m.get('downloadUrls') is not None:
            for k1 in m.get('downloadUrls'):
                temp_model = main_models.GetYzdInstanceTaskResultResponseBodyDataDownloadUrls()
                self.download_urls.append(temp_model.from_map(k1))

        if m.get('resultCnt') is not None:
            self.result_cnt = m.get('resultCnt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('timeDuration') is not None:
            self.time_duration = m.get('timeDuration')

        return self

class GetYzdInstanceTaskResultResponseBodyDataDownloadUrls(DaraModel):
    def __init__(
        self,
        pwd: str = None,
        url: str = None,
    ):
        self.pwd = pwd
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pwd is not None:
            result['pwd'] = self.pwd

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pwd') is not None:
            self.pwd = m.get('pwd')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

