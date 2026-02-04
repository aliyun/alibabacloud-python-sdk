# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSynchronizationObjectModifyStatusResponseBody(DaraModel):
    def __init__(
        self,
        data_initialization_status: main_models.DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus = None,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        precheck_status: main_models.DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        status: str = None,
        structure_initialization_status: main_models.DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus = None,
        success: str = None,
    ):
        # The status of full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The status of incremental data synchronization.
        # 
        # >  This parameter and its sub-parameters will be removed in the future.
        self.data_synchronization_status = data_synchronization_status
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The error message returned if the task failed to modify the objects to be synchronized.
        self.error_message = error_message
        # The precheck status.
        self.precheck_status = precheck_status
        # The ID of the request.
        self.request_id = request_id
        # The status of the task that changes the objects to be synchronized. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **Migrating**: The task is running.
        # *   **Failed**: The task failed.
        # *   **Finished**: The task is completed.
        self.status = status
        # The status of schema synchronization.
        self.structure_initialization_status = structure_initialization_status
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()

        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if schema synchronization failed.
        self.error_message = error_message
        # The progress of schema synchronization. Unit: %.
        self.percent = percent
        # The number of tables whose schemas have been synchronized.
        self.progress = progress
        # The status of schema synchronization. Valid values:
        # 
        # *   **NotStarted**: Schema synchronization is not started.
        # *   **Migrating**: Schema synchronization is in progress.
        # *   **Failed**: Schema synchronization failed.
        # *   **Finished**: Schema synchronization is completed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        # The result of each precheck item.
        self.detail = detail
        # The precheck progress. Unit: %.
        self.percent = percent
        # The precheck status.
        self.status = status

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        # The precheck result. Valid values:
        # 
        # *   Success: The task passed the precheck.
        # *   Failed: The task failed to pass the precheck.
        self.check_status = check_status
        # The error message returned if the task failed to pass the precheck.
        # 
        # >  This parameter is returned only if the return value of the **CheckStatus** parameter is **Failed**.
        self.error_message = error_message
        # The name of the precheck item.
        self.item_name = item_name
        # The method to fix the precheck failure.
        # 
        # >  This parameter is returned only if the return value of the **CheckStatus** parameter is Failed.
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.item_name is not None:
            result['ItemName'] = self.item_name

        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        return self

class DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The synchronization latency, in seconds.
        self.delay = delay
        # The error message returned if incremental data synchronization failed.
        self.error_message = error_message
        # The progress of incremental data synchronization. Unit: %.
        self.percent = percent
        # The status of incremental data synchronization. Valid values:
        # 
        # *   **NotStarted**: Incremental data synchronization is not started.
        # *   **Migrating**: Incremental data synchronization is in progress.
        # *   **Failed**: Incremental data synchronization failed.
        # *   **Finished**: Incremental data synchronization is completed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if full data synchronization failed.
        self.error_message = error_message
        # The progress of full data synchronization. Unit: %.
        self.percent = percent
        # The number of records that have been synchronized during full data synchronization.
        self.progress = progress
        # The status of full data synchronization. Valid values:
        # 
        # *   **NotStarted**: Full data synchronization is not started.
        # *   **Migrating**: Full data synchronization is in progress.
        # *   **Failed**: Full data synchronization failed.
        # *   **Finished**: Full data synchronization is completed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

