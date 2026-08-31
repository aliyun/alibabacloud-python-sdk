# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeLifecyclePolicyLogsResponseBody(DaraModel):
    def __init__(
        self,
        lifecycle_policy_logs: List[main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The execution logs of the lifecycle management policy.
        self.lifecycle_policy_logs = lifecycle_policy_logs
        # The page number.
        self.page_number = page_number
        # The number of log entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The request status. Valid values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success
        # The total number of log entries.
        self.total_count = total_count

    def validate(self):
        if self.lifecycle_policy_logs:
            for v1 in self.lifecycle_policy_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LifecyclePolicyLogs'] = []
        if self.lifecycle_policy_logs is not None:
            for k1 in self.lifecycle_policy_logs:
                result['LifecyclePolicyLogs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lifecycle_policy_logs = []
        if m.get('LifecyclePolicyLogs') is not None:
            for k1 in m.get('LifecyclePolicyLogs'):
                temp_model = main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogs()
                self.lifecycle_policy_logs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        delete_rules: List[main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsDeleteRules] = None,
        paths: List[str] = None,
        retrieve_rules: List[main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsRetrieveRules] = None,
        status: str = None,
        storage_type: str = None,
        summary: str = None,
        transit_rules: List[main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsTransitRules] = None,
    ):
        # The time when the task was created. The time follows the ISO 8601 standard in UTC. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The file data expiration and deletion rules. A maximum of one rule can be configured.
        self.delete_rules = delete_rules
        # The execution paths of the specified retrieval task.
        self.paths = paths
        # The file data retrieval rules.
        self.retrieve_rules = retrieve_rules
        # The status of the data retrieval task. Valid values:
        # - PENDING: Being created.
        # - RUNNING: Running.
        # - STOPPED: Stopped.
        # - FINISHED: Finished.
        # - FAILED: Failed.
        self.status = status
        # The tiered storage type. Valid values:
        # - InfrequentAccess: IA storage class (default).
        # - Archive: Archive storage.
        self.storage_type = storage_type
        # The task overview.
        self.summary = summary
        # The file data transit rules.
        self.transit_rules = transit_rules

    def validate(self):
        if self.delete_rules:
            for v1 in self.delete_rules:
                 if v1:
                    v1.validate()
        if self.retrieve_rules:
            for v1 in self.retrieve_rules:
                 if v1:
                    v1.validate()
        if self.transit_rules:
            for v1 in self.transit_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['DeleteRules'] = []
        if self.delete_rules is not None:
            for k1 in self.delete_rules:
                result['DeleteRules'].append(k1.to_map() if k1 else None)

        if self.paths is not None:
            result['Paths'] = self.paths

        result['RetrieveRules'] = []
        if self.retrieve_rules is not None:
            for k1 in self.retrieve_rules:
                result['RetrieveRules'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.summary is not None:
            result['Summary'] = self.summary

        result['TransitRules'] = []
        if self.transit_rules is not None:
            for k1 in self.transit_rules:
                result['TransitRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.delete_rules = []
        if m.get('DeleteRules') is not None:
            for k1 in m.get('DeleteRules'):
                temp_model = main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsDeleteRules()
                self.delete_rules.append(temp_model.from_map(k1))

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        self.retrieve_rules = []
        if m.get('RetrieveRules') is not None:
            for k1 in m.get('RetrieveRules'):
                temp_model = main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsRetrieveRules()
                self.retrieve_rules.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        self.transit_rules = []
        if m.get('TransitRules') is not None:
            for k1 in m.get('TransitRules'):
                temp_model = main_models.DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsTransitRules()
                self.transit_rules.append(temp_model.from_map(k1))

        return self

class DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsTransitRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The attribute of the rule.
        # 
        # Valid values:
        # - Atime: the last access time of the file.
        self.attribute = attribute
        # The threshold of the rule.
        # 
        # Valid values:
        # - If Attribute is set to Atime, this parameter specifies the number of days since the file was last accessed. Valid values: 1 to 365.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsRetrieveRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The attribute of the rule. Valid values:
        # - RetrieveType: the retrieval method.
        self.attribute = attribute
        # The threshold of the rule. Valid values:
        # - RetrieveType
        #     - AfterVisit: Supported when LifecyclePolicyType=Auto. Indicates best-effort recall on visit.
        #     - All: Supported when LifecyclePolicyType=OnDemand. Indicates retrieving all data.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class DescribeLifecyclePolicyLogsResponseBodyLifecyclePolicyLogsDeleteRules(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        threshold: str = None,
    ):
        # The attribute of the rule.
        # 
        # Valid values:
        # - Atime: the last access time of the file.
        self.attribute = attribute
        # The threshold of the rule.
        # 
        # Valid values:
        # - If Attribute is set to Atime, this parameter specifies the number of days since the file was last accessed. Valid values: 1 to 365.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

