# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryEmbeddedInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryEmbeddedInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The embedded information of the reports under the organization.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryEmbeddedInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryEmbeddedInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        detail: main_models.QueryEmbeddedInfoResponseBodyResultDetail = None,
        embedded_count: int = None,
        max_count: int = None,
    ):
        # Embed the statistics of the work.
        self.detail = detail
        # The number of reports that are currently embedded.
        self.embedded_count = embedded_count
        # The maximum number of reports that can be embedded.
        self.max_count = max_count

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.embedded_count is not None:
            result['EmbeddedCount'] = self.embedded_count

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = main_models.QueryEmbeddedInfoResponseBodyResultDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('EmbeddedCount') is not None:
            self.embedded_count = m.get('EmbeddedCount')

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        return self

class QueryEmbeddedInfoResponseBodyResultDetail(DaraModel):
    def __init__(
        self,
        dashboard_offline_query: int = None,
        page: int = None,
        report: int = None,
    ):
        # The number of embedded self-service fetching.
        self.dashboard_offline_query = dashboard_offline_query
        # The number of embedded dashboards.
        self.page = page
        # The number of embedded spreadsheets.
        self.report = report

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_offline_query is not None:
            result['DashboardOfflineQuery'] = self.dashboard_offline_query

        if self.page is not None:
            result['Page'] = self.page

        if self.report is not None:
            result['Report'] = self.report

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DashboardOfflineQuery') is not None:
            self.dashboard_offline_query = m.get('DashboardOfflineQuery')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Report') is not None:
            self.report = m.get('Report')

        return self

