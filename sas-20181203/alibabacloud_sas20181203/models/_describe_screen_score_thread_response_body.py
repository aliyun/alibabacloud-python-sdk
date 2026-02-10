# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeScreenScoreThreadResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeScreenScoreThreadResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeScreenScoreThreadResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeScreenScoreThreadResponseBodyData(DaraModel):
    def __init__(
        self,
        socre_thread: List[str] = None,
        socre_thread_date: List[str] = None,
    ):
        # The trends of the scores on the security dashboard.
        self.socre_thread = socre_thread
        # The dates of the scores on the security dashboard.
        self.socre_thread_date = socre_thread_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.socre_thread is not None:
            result['SocreThread'] = self.socre_thread

        if self.socre_thread_date is not None:
            result['SocreThreadDate'] = self.socre_thread_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SocreThread') is not None:
            self.socre_thread = m.get('SocreThread')

        if m.get('SocreThreadDate') is not None:
            self.socre_thread_date = m.get('SocreThreadDate')

        return self

