# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DatasetConfig(DaraModel):
    def __init__(
        self,
        insights: main_models.InsightsConfig = None,
        reverse_image: main_models.ReverseImageConfig = None,
        smart_cluster: main_models.SmartClusterConfig = None,
    ):
        # The content awareness configuration.
        self.insights = insights
        self.reverse_image = reverse_image
        # The intelligent clustering configuration.
        self.smart_cluster = smart_cluster

    def validate(self):
        if self.insights:
            self.insights.validate()
        if self.reverse_image:
            self.reverse_image.validate()
        if self.smart_cluster:
            self.smart_cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insights is not None:
            result['Insights'] = self.insights.to_map()

        if self.reverse_image is not None:
            result['ReverseImage'] = self.reverse_image.to_map()

        if self.smart_cluster is not None:
            result['SmartCluster'] = self.smart_cluster.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Insights') is not None:
            temp_model = main_models.InsightsConfig()
            self.insights = temp_model.from_map(m.get('Insights'))

        if m.get('ReverseImage') is not None:
            temp_model = main_models.ReverseImageConfig()
            self.reverse_image = temp_model.from_map(m.get('ReverseImage'))

        if m.get('SmartCluster') is not None:
            temp_model = main_models.SmartClusterConfig()
            self.smart_cluster = temp_model.from_map(m.get('SmartCluster'))

        return self

