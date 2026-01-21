# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutEventRuleTargetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        failed_contact_parameters: main_models.PutEventRuleTargetsResponseBodyFailedContactParameters = None,
        failed_fc_parameters: main_models.PutEventRuleTargetsResponseBodyFailedFcParameters = None,
        failed_mns_parameters: main_models.PutEventRuleTargetsResponseBodyFailedMnsParameters = None,
        failed_parameter_count: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # This parameter is returned if the specified alert contact groups in the request failed to be created or modified.
        self.failed_contact_parameters = failed_contact_parameters
        # This parameter is returned if the specified functions in the request failed to be created or modified in Function Compute.
        self.failed_fc_parameters = failed_fc_parameters
        # This parameter is returned if the specified queues in the request failed to be created or modified in SMQ.
        self.failed_mns_parameters = failed_mns_parameters
        # The number of resources that failed to be created or modified.
        self.failed_parameter_count = failed_parameter_count
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.failed_contact_parameters:
            self.failed_contact_parameters.validate()
        if self.failed_fc_parameters:
            self.failed_fc_parameters.validate()
        if self.failed_mns_parameters:
            self.failed_mns_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.failed_contact_parameters is not None:
            result['FailedContactParameters'] = self.failed_contact_parameters.to_map()

        if self.failed_fc_parameters is not None:
            result['FailedFcParameters'] = self.failed_fc_parameters.to_map()

        if self.failed_mns_parameters is not None:
            result['FailedMnsParameters'] = self.failed_mns_parameters.to_map()

        if self.failed_parameter_count is not None:
            result['FailedParameterCount'] = self.failed_parameter_count

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

        if m.get('FailedContactParameters') is not None:
            temp_model = main_models.PutEventRuleTargetsResponseBodyFailedContactParameters()
            self.failed_contact_parameters = temp_model.from_map(m.get('FailedContactParameters'))

        if m.get('FailedFcParameters') is not None:
            temp_model = main_models.PutEventRuleTargetsResponseBodyFailedFcParameters()
            self.failed_fc_parameters = temp_model.from_map(m.get('FailedFcParameters'))

        if m.get('FailedMnsParameters') is not None:
            temp_model = main_models.PutEventRuleTargetsResponseBodyFailedMnsParameters()
            self.failed_mns_parameters = temp_model.from_map(m.get('FailedMnsParameters'))

        if m.get('FailedParameterCount') is not None:
            self.failed_parameter_count = m.get('FailedParameterCount')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PutEventRuleTargetsResponseBodyFailedMnsParameters(DaraModel):
    def __init__(
        self,
        mns_parameter: List[main_models.PutEventRuleTargetsResponseBodyFailedMnsParametersMnsParameter] = None,
    ):
        self.mns_parameter = mns_parameter

    def validate(self):
        if self.mns_parameter:
            for v1 in self.mns_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MnsParameter'] = []
        if self.mns_parameter is not None:
            for k1 in self.mns_parameter:
                result['MnsParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mns_parameter = []
        if m.get('MnsParameter') is not None:
            for k1 in m.get('MnsParameter'):
                temp_model = main_models.PutEventRuleTargetsResponseBodyFailedMnsParametersMnsParameter()
                self.mns_parameter.append(temp_model.from_map(k1))

        return self

class PutEventRuleTargetsResponseBodyFailedMnsParametersMnsParameter(DaraModel):
    def __init__(
        self,
        id: int = None,
        queue: str = None,
        region: str = None,
    ):
        # The ID of the recipient.
        self.id = id
        # The name of the MNS queue.
        self.queue = queue
        # The region ID.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class PutEventRuleTargetsResponseBodyFailedFcParameters(DaraModel):
    def __init__(
        self,
        fc_parameter: List[main_models.PutEventRuleTargetsResponseBodyFailedFcParametersFcParameter] = None,
    ):
        self.fc_parameter = fc_parameter

    def validate(self):
        if self.fc_parameter:
            for v1 in self.fc_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FcParameter'] = []
        if self.fc_parameter is not None:
            for k1 in self.fc_parameter:
                result['FcParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fc_parameter = []
        if m.get('FcParameter') is not None:
            for k1 in m.get('FcParameter'):
                temp_model = main_models.PutEventRuleTargetsResponseBodyFailedFcParametersFcParameter()
                self.fc_parameter.append(temp_model.from_map(k1))

        return self

class PutEventRuleTargetsResponseBodyFailedFcParametersFcParameter(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        id: int = None,
        region: str = None,
        service_name: str = None,
    ):
        # The name of the function.
        self.function_name = function_name
        # The ID of the recipient.
        self.id = id
        # The region ID.
        self.region = region
        # The name of the Function Compute service.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.id is not None:
            result['Id'] = self.id

        if self.region is not None:
            result['Region'] = self.region

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class PutEventRuleTargetsResponseBodyFailedContactParameters(DaraModel):
    def __init__(
        self,
        contact_parameter: List[main_models.PutEventRuleTargetsResponseBodyFailedContactParametersContactParameter] = None,
    ):
        self.contact_parameter = contact_parameter

    def validate(self):
        if self.contact_parameter:
            for v1 in self.contact_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactParameter'] = []
        if self.contact_parameter is not None:
            for k1 in self.contact_parameter:
                result['ContactParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_parameter = []
        if m.get('ContactParameter') is not None:
            for k1 in m.get('ContactParameter'):
                temp_model = main_models.PutEventRuleTargetsResponseBodyFailedContactParametersContactParameter()
                self.contact_parameter.append(temp_model.from_map(k1))

        return self

class PutEventRuleTargetsResponseBodyFailedContactParametersContactParameter(DaraModel):
    def __init__(
        self,
        contact_group_name: str = None,
        id: int = None,
        level: str = None,
    ):
        # The name of the alert contact group.
        self.contact_group_name = contact_group_name
        # The ID of the recipient.
        self.id = id
        # The alert notification methods. Valid values:
        # 
        # 4: Alert notifications are sent by using DingTalk and emails.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

