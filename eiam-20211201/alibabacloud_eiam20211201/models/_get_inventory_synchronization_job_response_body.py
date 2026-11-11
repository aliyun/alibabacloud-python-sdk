# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetInventorySynchronizationJobResponseBody(DaraModel):
    def __init__(
        self,
        inventory_synchronization_job: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJob = None,
        request_id: str = None,
    ):
        # The inventory synchronization job.
        self.inventory_synchronization_job = inventory_synchronization_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.inventory_synchronization_job:
            self.inventory_synchronization_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inventory_synchronization_job is not None:
            result['InventorySynchronizationJob'] = self.inventory_synchronization_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InventorySynchronizationJob') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJob()
            self.inventory_synchronization_job = temp_model.from_map(m.get('InventorySynchronizationJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJob(DaraModel):
    def __init__(
        self,
        description: str = None,
        end_time: int = None,
        inventory_source_id: str = None,
        inventory_synchronization_job_id: str = None,
        result: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResult = None,
        start_time: int = None,
        status: str = None,
        trigger_type: str = None,
    ):
        # The synchronization job description.
        self.description = description
        # The synchronization end time.
        self.end_time = end_time
        # The synchronization target ID.
        self.inventory_source_id = inventory_source_id
        # The ID of the synchronization task.
        self.inventory_synchronization_job_id = inventory_synchronization_job_id
        # The synchronization node task result.
        self.result = result
        # The synchronization start time.
        self.start_time = start_time
        # The synchronization job status.
        self.status = status
        # The synchronization trigger type.
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
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResult(DaraModel):
    def __init__(
        self,
        agent_statistics: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatistics = None,
        asset_statistics: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatistics = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The agent synchronization result statistics.
        self.agent_statistics = agent_statistics
        # The asset synchronization result statistics.
        self.asset_statistics = asset_statistics
        # The error code of the synchronization result.
        self.error_code = error_code
        # The error message description of the synchronization result.
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
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatistics()
            self.agent_statistics = temp_model.from_map(m.get('AgentStatistics'))

        if m.get('AssetStatistics') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatistics()
            self.asset_statistics = temp_model.from_map(m.get('AssetStatistics'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatistics(DaraModel):
    def __init__(
        self,
        created: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsCreated = None,
        deleted: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsDeleted = None,
        same: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsSame = None,
        updated: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsUpdated = None,
    ):
        # The creation result statistics.
        self.created = created
        # The deletion result statistics.
        self.deleted = deleted
        # The unchanged result statistics.
        self.same = same
        # The update result statistics.
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
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Same') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAssetStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatistics(DaraModel):
    def __init__(
        self,
        created: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsCreated = None,
        deleted: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsDeleted = None,
        same: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsSame = None,
        updated: main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsUpdated = None,
    ):
        # The creation result statistics.
        self.created = created
        # The deletion result statistics.
        self.deleted = deleted
        # The unchanged result statistics.
        self.same = same
        # The update result statistics.
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
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Same') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

class GetInventorySynchronizationJobResponseBodyInventorySynchronizationJobResultAgentStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The failure count.
        self.failed = failed
        # The skipped count.
        self.skipped = skipped
        # The success count.
        self.success = success
        # The total count.
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

