# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ObserveGroupDiscoverRulesPreview(DaraModel):
    def __init__(
        self,
        catalog_revision: str = None,
        count: int = None,
        entity_summaries: List[main_models.ObserveGroupEntitySummary] = None,
        filtered_count: int = None,
        instances: List[main_models.ObserveGroupInstance] = None,
        main_count: int = None,
        max_results: int = None,
        next_token: str = None,
        related_count: int = None,
        rule_counts: List[main_models.ObserveGroupRuleCount] = None,
        total_count: int = None,
    ):
        # The global association catalog version used for this preview.
        self.catalog_revision = catalog_revision
        # The number of entities returned on this page.
        self.count = count
        # The primary entities, associated sub-entities, and total count by entity type.
        self.entity_summaries = entity_summaries
        # The total count after filtering by entity role, type, and keyword.
        self.filtered_count = filtered_count
        # The list of matched entities on this page.
        self.instances = instances
        # The deduplicated count of primary entities.
        self.main_count = main_count
        # The maximum number of entities returned on this page.
        self.max_results = max_results
        # The next page token, which is empty if there is no next page.
        self.next_token = next_token
        # The deduplicated count of associated sub-entities.
        self.related_count = related_count
        # The primary entities, associated sub-entities, and total count by rule.
        self.rule_counts = rule_counts
        # The deduplicated total count of entities.
        self.total_count = total_count

    def validate(self):
        if self.entity_summaries:
            for v1 in self.entity_summaries:
                 if v1:
                    v1.validate()
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.rule_counts:
            for v1 in self.rule_counts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_revision is not None:
            result['catalogRevision'] = self.catalog_revision

        if self.count is not None:
            result['count'] = self.count

        result['entitySummaries'] = []
        if self.entity_summaries is not None:
            for k1 in self.entity_summaries:
                result['entitySummaries'].append(k1.to_map() if k1 else None)

        if self.filtered_count is not None:
            result['filteredCount'] = self.filtered_count

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.main_count is not None:
            result['mainCount'] = self.main_count

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.related_count is not None:
            result['relatedCount'] = self.related_count

        result['ruleCounts'] = []
        if self.rule_counts is not None:
            for k1 in self.rule_counts:
                result['ruleCounts'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogRevision') is not None:
            self.catalog_revision = m.get('catalogRevision')

        if m.get('count') is not None:
            self.count = m.get('count')

        self.entity_summaries = []
        if m.get('entitySummaries') is not None:
            for k1 in m.get('entitySummaries'):
                temp_model = main_models.ObserveGroupEntitySummary()
                self.entity_summaries.append(temp_model.from_map(k1))

        if m.get('filteredCount') is not None:
            self.filtered_count = m.get('filteredCount')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.ObserveGroupInstance()
                self.instances.append(temp_model.from_map(k1))

        if m.get('mainCount') is not None:
            self.main_count = m.get('mainCount')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('relatedCount') is not None:
            self.related_count = m.get('relatedCount')

        self.rule_counts = []
        if m.get('ruleCounts') is not None:
            for k1 in m.get('ruleCounts'):
                temp_model = main_models.ObserveGroupRuleCount()
                self.rule_counts.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

