# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListInventorySynchronizationJobsResponseBody(DaraModel):
    def __init__(
        self,
        inventory_synchronization_jobs: List[main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The inventory synchronization jobs.
        self.inventory_synchronization_jobs = inventory_synchronization_jobs
        # The maximum number of returned results.
        self.max_results = max_results
        # The pagination token returned by the current call, which is used to retrieve the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.inventory_synchronization_jobs:
            for v1 in self.inventory_synchronization_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InventorySynchronizationJobs'] = []
        if self.inventory_synchronization_jobs is not None:
            for k1 in self.inventory_synchronization_jobs:
                result['InventorySynchronizationJobs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inventory_synchronization_jobs = []
        if m.get('InventorySynchronizationJobs') is not None:
            for k1 in m.get('InventorySynchronizationJobs'):
                temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobs()
                self.inventory_synchronization_jobs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobs(DaraModel):
    def __init__(
        self,
        description: str = None,
        end_time: int = None,
        inventory_source_id: str = None,
        inventory_synchronization_job_id: str = None,
        result: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResult = None,
        start_time: int = None,
        status: str = None,
        trigger_type: str = None,
    ):
        # The description of the synchronization job.
        self.description = description
        # The end time of the synchronization job.
        self.end_time = end_time
        # The IDs of the synchronization targets.
        self.inventory_source_id = inventory_source_id
        # The ID of the synchronization job.
        self.inventory_synchronization_job_id = inventory_synchronization_job_id
        # The task result of the synchronization node.
        self.result = result
        # The start time of the synchronization job.
        self.start_time = start_time
        # The status of the synchronization job.
        self.status = status
        # The trigger type of the synchronization job.
        self.trigger_type = trigger_type

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.inventory_source_id is not None:
            result['InventorySourceId'] = self.inventory_source_id

        if self.inventory_synchronization_job_id is not None:
            result['InventorySynchronizationJobId'] = self.inventory_synchronization_job_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InventorySourceId') is not None:
            self.inventory_source_id = m.get('InventorySourceId')

        if m.get('InventorySynchronizationJobId') is not None:
            self.inventory_synchronization_job_id = m.get('InventorySynchronizationJobId')

        if m.get('Result') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResult(DaraModel):
    def __init__(
        self,
        agent_statistics: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatistics = None,
        asset_statistics: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatistics = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The statistics of the agent synchronization results.
        self.agent_statistics = agent_statistics
        # The statistics of the asset synchronization results.
        self.asset_statistics = asset_statistics
        # The error code of the synchronization result.
        self.error_code = error_code
        # The error message of the synchronization result.
        self.error_message = error_message

    def validate(self):
        if self.agent_statistics:
            self.agent_statistics.validate()
        if self.asset_statistics:
            self.asset_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_statistics is not None:
            result['AgentStatistics'] = self.agent_statistics.to_map()

        if self.asset_statistics is not None:
            result['AssetStatistics'] = self.asset_statistics.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatistics') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatistics()
            self.agent_statistics = temp_model.from_map(m.get('AgentStatistics'))

        if m.get('AssetStatistics') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatistics()
            self.asset_statistics = temp_model.from_map(m.get('AssetStatistics'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatistics(DaraModel):
    def __init__(
        self,
        created: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsCreated = None,
        deleted: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsDeleted = None,
        same: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsSame = None,
        updated: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsUpdated = None,
    ):
        # The statistics of the creation results.
        self.created = created
        # The statistics of the deletion results.
        self.deleted = deleted
        # The statistics of the unchanged results.
        self.same = same
        # The statistics of the update results.
        self.updated = updated

    def validate(self):
        if self.created:
            self.created.validate()
        if self.deleted:
            self.deleted.validate()
        if self.same:
            self.same.validate()
        if self.updated:
            self.updated.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['Created'] = self.created.to_map()

        if self.deleted is not None:
            result['Deleted'] = self.deleted.to_map()

        if self.same is not None:
            result['Same'] = self.same.to_map()

        if self.updated is not None:
            result['Updated'] = self.updated.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Created') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Same') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAssetStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatistics(DaraModel):
    def __init__(
        self,
        created: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsCreated = None,
        deleted: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsDeleted = None,
        same: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsSame = None,
        updated: main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsUpdated = None,
    ):
        # The statistics of the creation results.
        self.created = created
        # The statistics of the deletion results.
        self.deleted = deleted
        # The statistics of the unchanged results.
        self.same = same
        # The statistics of the update results.
        self.updated = updated

    def validate(self):
        if self.created:
            self.created.validate()
        if self.deleted:
            self.deleted.validate()
        if self.same:
            self.same.validate()
        if self.updated:
            self.updated.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['Created'] = self.created.to_map()

        if self.deleted is not None:
            result['Deleted'] = self.deleted.to_map()

        if self.same is not None:
            result['Same'] = self.same.to_map()

        if self.updated is not None:
            result['Updated'] = self.updated.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Created') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Same') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListInventorySynchronizationJobsResponseBodyInventorySynchronizationJobsResultAgentStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed creations.
        self.failed = failed
        # The number of skipped creations.
        self.skipped = skipped
        # The number of successful creations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

