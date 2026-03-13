# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class GetEnrolledAccountResponseBody(DaraModel):
    def __init__(
        self,
        account_uid: int = None,
        baseline_id: str = None,
        baseline_items: List[main_models.GetEnrolledAccountResponseBodyBaselineItems] = None,
        create_time: str = None,
        display_name: str = None,
        error_info: main_models.GetEnrolledAccountResponseBodyErrorInfo = None,
        folder_id: str = None,
        initialized: bool = None,
        inputs: main_models.GetEnrolledAccountResponseBodyInputs = None,
        master_account_uid: int = None,
        payer_account_uid: int = None,
        progress: List[main_models.GetEnrolledAccountResponseBodyProgress] = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The account ID.
        self.account_uid = account_uid
        # The ID of the baseline that is implemented.
        self.baseline_id = baseline_id
        # The array that contains baseline items.
        self.baseline_items = baseline_items
        # The time when the account was created.
        self.create_time = create_time
        # The display name of the account.
        self.display_name = display_name
        # The error message.
        # 
        # >  This parameter is returned if the value of `Status` is `Failed` or `ScheduleFailed`.
        self.error_info = error_info
        # The ID of the parent folder.
        self.folder_id = folder_id
        # Indicates whether the initialization is complete. Valid values:
        # 
        # *   false
        # *   true
        self.initialized = initialized
        # Input parameters used to create an account.
        self.inputs = inputs
        # The ID of the management account of the resource directory to which the account belongs.
        self.master_account_uid = master_account_uid
        # The ID of the settlement account.
        self.payer_account_uid = payer_account_uid
        # The progress of the applying the baseline to the account.
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The status of the account. Valid values:
        # 
        # *   Pending: The account is pending to be created.
        # *   Running: The account is being created.
        # *   Finished: The account is created.
        # *   Failed: The account fails to be created.
        # *   Scheduling: The account is being scheduled.
        # *   ScheduleFailed: The account fails to be scheduled.
        self.status = status
        # The update time.
        self.update_time = update_time

    def validate(self):
        if self.baseline_items:
            for v1 in self.baseline_items:
                 if v1:
                    v1.validate()
        if self.error_info:
            self.error_info.validate()
        if self.inputs:
            self.inputs.validate()
        if self.progress:
            for v1 in self.progress:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k1 in self.baseline_items:
                result['BaselineItems'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info.to_map()

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.initialized is not None:
            result['Initialized'] = self.initialized

        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()

        if self.master_account_uid is not None:
            result['MasterAccountUid'] = self.master_account_uid

        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid

        result['Progress'] = []
        if self.progress is not None:
            for k1 in self.progress:
                result['Progress'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k1 in m.get('BaselineItems'):
                temp_model = main_models.GetEnrolledAccountResponseBodyBaselineItems()
                self.baseline_items.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ErrorInfo') is not None:
            temp_model = main_models.GetEnrolledAccountResponseBodyErrorInfo()
            self.error_info = temp_model.from_map(m.get('ErrorInfo'))

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('Initialized') is not None:
            self.initialized = m.get('Initialized')

        if m.get('Inputs') is not None:
            temp_model = main_models.GetEnrolledAccountResponseBodyInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('MasterAccountUid') is not None:
            self.master_account_uid = m.get('MasterAccountUid')

        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')

        self.progress = []
        if m.get('Progress') is not None:
            for k1 in m.get('Progress'):
                temp_model = main_models.GetEnrolledAccountResponseBodyProgress()
                self.progress.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetEnrolledAccountResponseBodyProgress(DaraModel):
    def __init__(
        self,
        name: str = None,
        status: str = None,
    ):
        # The name of the baseline item.
        self.name = name
        # The status of applying the baseline to the account. Valid values:
        # 
        # *   Pending: The baseline is pending to be applied to the account.
        # *   Running: The baseline is being applied to the account.
        # *   Finished: : The baseline is applied to the account.
        # *   Failed: : The baseline fails to be applied to the account.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetEnrolledAccountResponseBodyInputs(DaraModel):
    def __init__(
        self,
        account_name_prefix: str = None,
        account_uid: int = None,
        baseline_items: List[main_models.GetEnrolledAccountResponseBodyInputsBaselineItems] = None,
        display_name: str = None,
        folder_id: str = None,
        payer_account_uid: int = None,
        tag: List[main_models.GetEnrolledAccountResponseBodyInputsTag] = None,
    ):
        # The prefix of the account name.
        self.account_name_prefix = account_name_prefix
        # The account ID.
        self.account_uid = account_uid
        # The baseline items.
        self.baseline_items = baseline_items
        # The display name of the account.
        self.display_name = display_name
        # The ID of the parent folder.
        self.folder_id = folder_id
        # The ID of the settlement account.
        self.payer_account_uid = payer_account_uid
        # The tag.
        self.tag = tag

    def validate(self):
        if self.baseline_items:
            for v1 in self.baseline_items:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name_prefix is not None:
            result['AccountNamePrefix'] = self.account_name_prefix

        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid

        result['BaselineItems'] = []
        if self.baseline_items is not None:
            for k1 in self.baseline_items:
                result['BaselineItems'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNamePrefix') is not None:
            self.account_name_prefix = m.get('AccountNamePrefix')

        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')

        self.baseline_items = []
        if m.get('BaselineItems') is not None:
            for k1 in m.get('BaselineItems'):
                temp_model = main_models.GetEnrolledAccountResponseBodyInputsBaselineItems()
                self.baseline_items.append(temp_model.from_map(k1))

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.GetEnrolledAccountResponseBodyInputsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class GetEnrolledAccountResponseBodyInputsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEnrolledAccountResponseBodyInputsBaselineItems(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        skip: bool = None,
        version: str = None,
    ):
        # The configurations of the baseline item.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # Indicates whether baseline item is skipped. Valid values:
        # 
        # *   false
        # *   true
        self.skip = skip
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetEnrolledAccountResponseBodyErrorInfo(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        recommend: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The recommended solution.
        self.recommend = recommend
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.recommend is not None:
            result['Recommend'] = self.recommend

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEnrolledAccountResponseBodyBaselineItems(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        skip: bool = None,
        version: str = None,
    ):
        # The configuration of the baseline item.
        self.config = config
        # The name of the baseline item.
        self.name = name
        # Indicates whether baseline item is skipped. Valid values:
        # 
        # *   false
        # *   true
        self.skip = skip
        # The version of the baseline item.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.name is not None:
            result['Name'] = self.name

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

