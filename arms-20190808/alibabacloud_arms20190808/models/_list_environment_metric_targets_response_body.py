# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvironmentMetricTargetsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListEnvironmentMetricTargetsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The struct returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListEnvironmentMetricTargetsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEnvironmentMetricTargetsResponseBodyData(DaraModel):
    def __init__(
        self,
        active_targets: List[main_models.ListEnvironmentMetricTargetsResponseBodyDataActiveTargets] = None,
        dropped_targets: List[main_models.ListEnvironmentMetricTargetsResponseBodyDataDroppedTargets] = None,
    ):
        # The active targets.
        self.active_targets = active_targets
        # The deleted targets.
        self.dropped_targets = dropped_targets

    def validate(self):
        if self.active_targets:
            for v1 in self.active_targets:
                 if v1:
                    v1.validate()
        if self.dropped_targets:
            for v1 in self.dropped_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActiveTargets'] = []
        if self.active_targets is not None:
            for k1 in self.active_targets:
                result['ActiveTargets'].append(k1.to_map() if k1 else None)

        result['DroppedTargets'] = []
        if self.dropped_targets is not None:
            for k1 in self.dropped_targets:
                result['DroppedTargets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.active_targets = []
        if m.get('ActiveTargets') is not None:
            for k1 in m.get('ActiveTargets'):
                temp_model = main_models.ListEnvironmentMetricTargetsResponseBodyDataActiveTargets()
                self.active_targets.append(temp_model.from_map(k1))

        self.dropped_targets = []
        if m.get('DroppedTargets') is not None:
            for k1 in m.get('DroppedTargets'):
                temp_model = main_models.ListEnvironmentMetricTargetsResponseBodyDataDroppedTargets()
                self.dropped_targets.append(temp_model.from_map(k1))

        return self

class ListEnvironmentMetricTargetsResponseBodyDataDroppedTargets(DaraModel):
    def __init__(
        self,
        discovered_labels: Dict[str, str] = None,
        global_url: str = None,
        health: str = None,
        labels: Dict[str, str] = None,
        last_error: str = None,
        last_scrape: str = None,
        last_scrape_duration: float = None,
        last_scrape_series: int = None,
        scrape_pool: str = None,
        scrape_url: str = None,
    ):
        # The tags used for service discovery.
        self.discovered_labels = discovered_labels
        # The URL of the target.
        self.global_url = global_url
        # The health status.
        self.health = health
        # The tags.
        self.labels = labels
        # The last error message.
        self.last_error = last_error
        # The last collection time.
        self.last_scrape = last_scrape
        # The duration of the last collection.
        self.last_scrape_duration = last_scrape_duration
        # The amount of metrics in the last collection.
        self.last_scrape_series = last_scrape_series
        # The name of the collection.
        self.scrape_pool = scrape_pool
        # The URL of the collection.
        self.scrape_url = scrape_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discovered_labels is not None:
            result['DiscoveredLabels'] = self.discovered_labels

        if self.global_url is not None:
            result['GlobalUrl'] = self.global_url

        if self.health is not None:
            result['Health'] = self.health

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.last_error is not None:
            result['LastError'] = self.last_error

        if self.last_scrape is not None:
            result['LastScrape'] = self.last_scrape

        if self.last_scrape_duration is not None:
            result['LastScrapeDuration'] = self.last_scrape_duration

        if self.last_scrape_series is not None:
            result['LastScrapeSeries'] = self.last_scrape_series

        if self.scrape_pool is not None:
            result['ScrapePool'] = self.scrape_pool

        if self.scrape_url is not None:
            result['ScrapeUrl'] = self.scrape_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredLabels') is not None:
            self.discovered_labels = m.get('DiscoveredLabels')

        if m.get('GlobalUrl') is not None:
            self.global_url = m.get('GlobalUrl')

        if m.get('Health') is not None:
            self.health = m.get('Health')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LastError') is not None:
            self.last_error = m.get('LastError')

        if m.get('LastScrape') is not None:
            self.last_scrape = m.get('LastScrape')

        if m.get('LastScrapeDuration') is not None:
            self.last_scrape_duration = m.get('LastScrapeDuration')

        if m.get('LastScrapeSeries') is not None:
            self.last_scrape_series = m.get('LastScrapeSeries')

        if m.get('ScrapePool') is not None:
            self.scrape_pool = m.get('ScrapePool')

        if m.get('ScrapeUrl') is not None:
            self.scrape_url = m.get('ScrapeUrl')

        return self

class ListEnvironmentMetricTargetsResponseBodyDataActiveTargets(DaraModel):
    def __init__(
        self,
        discovered_labels: Dict[str, str] = None,
        global_url: str = None,
        health: str = None,
        labels: Dict[str, str] = None,
        last_error: str = None,
        last_scrape: str = None,
        last_scrape_duration: float = None,
        last_scrape_series: int = None,
        scrape_pool: str = None,
        scrape_url: str = None,
    ):
        # The tags used for service discovery.
        self.discovered_labels = discovered_labels
        # The URL of the target.
        self.global_url = global_url
        # The health status.
        self.health = health
        # The tags.
        self.labels = labels
        # The last error message.
        self.last_error = last_error
        # The last collection time.
        self.last_scrape = last_scrape
        # The duration of the last collection.
        self.last_scrape_duration = last_scrape_duration
        # The amount of metrics in the last collection.
        self.last_scrape_series = last_scrape_series
        # The name of the collection.
        self.scrape_pool = scrape_pool
        # The URL of the collection.
        self.scrape_url = scrape_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discovered_labels is not None:
            result['DiscoveredLabels'] = self.discovered_labels

        if self.global_url is not None:
            result['GlobalUrl'] = self.global_url

        if self.health is not None:
            result['Health'] = self.health

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.last_error is not None:
            result['LastError'] = self.last_error

        if self.last_scrape is not None:
            result['LastScrape'] = self.last_scrape

        if self.last_scrape_duration is not None:
            result['LastScrapeDuration'] = self.last_scrape_duration

        if self.last_scrape_series is not None:
            result['LastScrapeSeries'] = self.last_scrape_series

        if self.scrape_pool is not None:
            result['ScrapePool'] = self.scrape_pool

        if self.scrape_url is not None:
            result['ScrapeUrl'] = self.scrape_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscoveredLabels') is not None:
            self.discovered_labels = m.get('DiscoveredLabels')

        if m.get('GlobalUrl') is not None:
            self.global_url = m.get('GlobalUrl')

        if m.get('Health') is not None:
            self.health = m.get('Health')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LastError') is not None:
            self.last_error = m.get('LastError')

        if m.get('LastScrape') is not None:
            self.last_scrape = m.get('LastScrape')

        if m.get('LastScrapeDuration') is not None:
            self.last_scrape_duration = m.get('LastScrapeDuration')

        if m.get('LastScrapeSeries') is not None:
            self.last_scrape_series = m.get('LastScrapeSeries')

        if m.get('ScrapePool') is not None:
            self.scrape_pool = m.get('ScrapePool')

        if m.get('ScrapeUrl') is not None:
            self.scrape_url = m.get('ScrapeUrl')

        return self

