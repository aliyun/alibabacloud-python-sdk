# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListFeatureConsistencyCheckJobScoreReportsResponseBody(DaraModel):
    def __init__(
        self,
        data_path: str = None,
        oss_path: str = None,
        reports_of_score_diff: List[main_models.ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff] = None,
        request_id: str = None,
    ):
        self.data_path = data_path
        self.oss_path = oss_path
        self.reports_of_score_diff = reports_of_score_diff
        self.request_id = request_id

    def validate(self):
        if self.reports_of_score_diff:
            for v1 in self.reports_of_score_diff:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_path is not None:
            result['DataPath'] = self.data_path

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        result['ReportsOfScoreDiff'] = []
        if self.reports_of_score_diff is not None:
            for k1 in self.reports_of_score_diff:
                result['ReportsOfScoreDiff'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPath') is not None:
            self.data_path = m.get('DataPath')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        self.reports_of_score_diff = []
        if m.get('ReportsOfScoreDiff') is not None:
            for k1 in m.get('ReportsOfScoreDiff'):
                temp_model = main_models.ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff()
                self.reports_of_score_diff.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFeatureConsistencyCheckJobScoreReportsResponseBodyReportsOfScoreDiff(DaraModel):
    def __init__(
        self,
        log_item_id: str = None,
        log_request_id: str = None,
        log_user_id: str = None,
        score_diff: str = None,
        score_diff_detail: str = None,
    ):
        self.log_item_id = log_item_id
        self.log_request_id = log_request_id
        self.log_user_id = log_user_id
        self.score_diff = score_diff
        self.score_diff_detail = score_diff_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id

        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        if self.score_diff is not None:
            result['ScoreDiff'] = self.score_diff

        if self.score_diff_detail is not None:
            result['ScoreDiffDetail'] = self.score_diff_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')

        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('ScoreDiff') is not None:
            self.score_diff = m.get('ScoreDiff')

        if m.get('ScoreDiffDetail') is not None:
            self.score_diff_detail = m.get('ScoreDiffDetail')

        return self

