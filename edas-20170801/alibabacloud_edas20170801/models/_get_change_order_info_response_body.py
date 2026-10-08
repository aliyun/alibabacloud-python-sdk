# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetChangeOrderInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        change_order_info: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfo = None,
    ):
        # The status of the API call or a POP error code.
        self.code = code
        # Additional information.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The details of the change process.
        self.change_order_info = change_order_info

    def validate(self):
        if self.change_order_info:
            self.change_order_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.change_order_info is not None:
            result['changeOrderInfo'] = self.change_order_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('changeOrderInfo') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfo()
            self.change_order_info = temp_model.from_map(m.get('changeOrderInfo'))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfo(DaraModel):
    def __init__(
        self,
        batch_count: int = None,
        batch_type: str = None,
        change_order_description: str = None,
        change_order_id: str = None,
        co_type: str = None,
        create_time: str = None,
        create_user_id: str = None,
        desc: str = None,
        pipeline_info_list: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoList = None,
        status: int = None,
        support_rollback: bool = None,
        targets: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoTargets = None,
        traffic_control: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoTrafficControl = None,
    ):
        # The number of batches for the change.
        self.batch_count = batch_count
        # The execution mode for the next batch in a phased release.
        # 
        # - Automatic: The next batch is automatically executed.
        # 
        # - Manual: The next batch is manually executed.
        self.batch_type = batch_type
        # The description of the change process.
        self.change_order_description = change_order_description
        # The ID of the change process.
        self.change_order_id = change_order_id
        # The classification of the change process.
        self.co_type = co_type
        # The time when the change process was created.
        self.create_time = create_time
        # The owner of the change process.
        self.create_user_id = create_user_id
        # The description of the change process.
        self.desc = desc
        self.pipeline_info_list = pipeline_info_list
        # The status of the change.
        # 
        # - 0: ready
        # 
        # - 1: in progress
        # 
        # - 2: successful
        # 
        # - 3: failed
        # 
        # - 6: stopped
        # 
        # - 7: partially successful
        # 
        # - 8: waiting for manual confirmation to proceed with the next batch in manual phased release mode
        # 
        # - 9: waiting for the next batch to be executed in automatic phased release mode
        # 
        # - 10: failed due to a system exception
        self.status = status
        # Indicates whether rollback is supported.
        # 
        # - true: Rollback is supported.
        # 
        # - false: Rollback is not supported.
        self.support_rollback = support_rollback
        self.targets = targets
        # The throttling rule.
        self.traffic_control = traffic_control

    def validate(self):
        if self.pipeline_info_list:
            self.pipeline_info_list.validate()
        if self.targets:
            self.targets.validate()
        if self.traffic_control:
            self.traffic_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count

        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.change_order_description is not None:
            result['ChangeOrderDescription'] = self.change_order_description

        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.co_type is not None:
            result['CoType'] = self.co_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.pipeline_info_list is not None:
            result['PipelineInfoList'] = self.pipeline_info_list.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.support_rollback is not None:
            result['SupportRollback'] = self.support_rollback

        if self.targets is not None:
            result['Targets'] = self.targets.to_map()

        if self.traffic_control is not None:
            result['TrafficControl'] = self.traffic_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')

        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('ChangeOrderDescription') is not None:
            self.change_order_description = m.get('ChangeOrderDescription')

        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('PipelineInfoList') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoList()
            self.pipeline_info_list = temp_model.from_map(m.get('PipelineInfoList'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportRollback') is not None:
            self.support_rollback = m.get('SupportRollback')

        if m.get('Targets') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoTargets()
            self.targets = temp_model.from_map(m.get('Targets'))

        if m.get('TrafficControl') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoTrafficControl()
            self.traffic_control = temp_model.from_map(m.get('TrafficControl'))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoTrafficControl(DaraModel):
    def __init__(
        self,
        routes: str = None,
        rules: str = None,
        tips: str = None,
    ):
        # The traffic forwarding rule.
        self.routes = routes
        # The routing rule for traffic.
        self.rules = rules
        # The description of the traffic rule.
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.routes is not None:
            result['Routes'] = self.routes

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.tips is not None:
            result['Tips'] = self.tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Routes') is not None:
            self.routes = m.get('Routes')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('Tips') is not None:
            self.tips = m.get('Tips')

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoTargets(DaraModel):
    def __init__(
        self,
        items: List[str] = None,
    ):
        self.items = items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoList(DaraModel):
    def __init__(
        self,
        pipeline_info: List[main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfo] = None,
    ):
        self.pipeline_info = pipeline_info

    def validate(self):
        if self.pipeline_info:
            for v1 in self.pipeline_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PipelineInfo'] = []
        if self.pipeline_info is not None:
            for k1 in self.pipeline_info:
                result['PipelineInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pipeline_info = []
        if m.get('PipelineInfo') is not None:
            for k1 in m.get('PipelineInfo'):
                temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfo()
                self.pipeline_info.append(temp_model.from_map(k1))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfo(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        pipeline_name: str = None,
        pipeline_status: int = None,
        stage_detail_list: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailList = None,
        stage_list: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageList = None,
        start_time: str = None,
        update_time: str = None,
    ):
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.pipeline_status = pipeline_status
        self.stage_detail_list = stage_detail_list
        self.stage_list = stage_list
        self.start_time = start_time
        self.update_time = update_time

    def validate(self):
        if self.stage_detail_list:
            self.stage_detail_list.validate()
        if self.stage_list:
            self.stage_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name

        if self.pipeline_status is not None:
            result['PipelineStatus'] = self.pipeline_status

        if self.stage_detail_list is not None:
            result['StageDetailList'] = self.stage_detail_list.to_map()

        if self.stage_list is not None:
            result['StageList'] = self.stage_list.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')

        if m.get('PipelineStatus') is not None:
            self.pipeline_status = m.get('PipelineStatus')

        if m.get('StageDetailList') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailList()
            self.stage_detail_list = temp_model.from_map(m.get('StageDetailList'))

        if m.get('StageList') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageList()
            self.stage_list = temp_model.from_map(m.get('StageList'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageList(DaraModel):
    def __init__(
        self,
        stage_info_dto: List[main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTO] = None,
    ):
        self.stage_info_dto = stage_info_dto

    def validate(self):
        if self.stage_info_dto:
            for v1 in self.stage_info_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StageInfoDTO'] = []
        if self.stage_info_dto is not None:
            for k1 in self.stage_info_dto:
                result['StageInfoDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stage_info_dto = []
        if m.get('StageInfoDTO') is not None:
            for k1 in m.get('StageInfoDTO'):
                temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTO()
                self.stage_info_dto.append(temp_model.from_map(k1))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTO(DaraModel):
    def __init__(
        self,
        stage_id: str = None,
        stage_name: str = None,
        stage_result_dto: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTO = None,
        status: int = None,
    ):
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.stage_result_dto = stage_result_dto
        self.status = status

    def validate(self):
        if self.stage_result_dto:
            self.stage_result_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.stage_result_dto is not None:
            result['StageResultDTO'] = self.stage_result_dto.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('StageResultDTO') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTO()
            self.stage_result_dto = temp_model.from_map(m.get('StageResultDTO'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTO(DaraModel):
    def __init__(
        self,
        instance_dtolist: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOList = None,
        service_stage: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOServiceStage = None,
    ):
        self.instance_dtolist = instance_dtolist
        self.service_stage = service_stage

    def validate(self):
        if self.instance_dtolist:
            self.instance_dtolist.validate()
        if self.service_stage:
            self.service_stage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_dtolist is not None:
            result['InstanceDTOList'] = self.instance_dtolist.to_map()

        if self.service_stage is not None:
            result['ServiceStage'] = self.service_stage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceDTOList') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOList()
            self.instance_dtolist = temp_model.from_map(m.get('InstanceDTOList'))

        if m.get('ServiceStage') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOServiceStage()
            self.service_stage = temp_model.from_map(m.get('ServiceStage'))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOServiceStage(DaraModel):
    def __init__(
        self,
        message: str = None,
        stage_id: str = None,
        stage_name: str = None,
        status: int = None,
    ):
        self.message = message
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOList(DaraModel):
    def __init__(
        self,
        instance_dto: List[main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTO] = None,
    ):
        self.instance_dto = instance_dto

    def validate(self):
        if self.instance_dto:
            for v1 in self.instance_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceDTO'] = []
        if self.instance_dto is not None:
            for k1 in self.instance_dto:
                result['InstanceDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_dto = []
        if m.get('InstanceDTO') is not None:
            for k1 in m.get('InstanceDTO'):
                temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTO()
                self.instance_dto.append(temp_model.from_map(k1))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTO(DaraModel):
    def __init__(
        self,
        instance_ip: str = None,
        instance_name: str = None,
        instance_stage_dtolist: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTOInstanceStageDTOList = None,
        pod_name: str = None,
        pod_status: str = None,
        status: int = None,
    ):
        self.instance_ip = instance_ip
        self.instance_name = instance_name
        self.instance_stage_dtolist = instance_stage_dtolist
        self.pod_name = pod_name
        self.pod_status = pod_status
        self.status = status

    def validate(self):
        if self.instance_stage_dtolist:
            self.instance_stage_dtolist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_stage_dtolist is not None:
            result['InstanceStageDTOList'] = self.instance_stage_dtolist.to_map()

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStageDTOList') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTOInstanceStageDTOList()
            self.instance_stage_dtolist = temp_model.from_map(m.get('InstanceStageDTOList'))

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('PodStatus') is not None:
            self.pod_status = m.get('PodStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTOInstanceStageDTOList(DaraModel):
    def __init__(
        self,
        instance_stage_dto: List[main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTOInstanceStageDTOListInstanceStageDTO] = None,
    ):
        self.instance_stage_dto = instance_stage_dto

    def validate(self):
        if self.instance_stage_dto:
            for v1 in self.instance_stage_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceStageDTO'] = []
        if self.instance_stage_dto is not None:
            for k1 in self.instance_stage_dto:
                result['InstanceStageDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_stage_dto = []
        if m.get('InstanceStageDTO') is not None:
            for k1 in m.get('InstanceStageDTO'):
                temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTOInstanceStageDTOListInstanceStageDTO()
                self.instance_stage_dto.append(temp_model.from_map(k1))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageListStageInfoDTOStageResultDTOInstanceDTOListInstanceDTOInstanceStageDTOListInstanceStageDTO(DaraModel):
    def __init__(
        self,
        finish_time: str = None,
        stage_id: str = None,
        stage_message: str = None,
        stage_name: str = None,
        start_time: str = None,
        status: int = None,
    ):
        self.finish_time = finish_time
        self.stage_id = stage_id
        self.stage_message = stage_message
        self.stage_name = stage_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_message is not None:
            result['StageMessage'] = self.stage_message

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageMessage') is not None:
            self.stage_message = m.get('StageMessage')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailList(DaraModel):
    def __init__(
        self,
        stage_detail_dto: List[main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTO] = None,
    ):
        self.stage_detail_dto = stage_detail_dto

    def validate(self):
        if self.stage_detail_dto:
            for v1 in self.stage_detail_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StageDetailDTO'] = []
        if self.stage_detail_dto is not None:
            for k1 in self.stage_detail_dto:
                result['StageDetailDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stage_detail_dto = []
        if m.get('StageDetailDTO') is not None:
            for k1 in m.get('StageDetailDTO'):
                temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTO()
                self.stage_detail_dto.append(temp_model.from_map(k1))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTO(DaraModel):
    def __init__(
        self,
        stage_id: str = None,
        stage_name: str = None,
        stage_status: int = None,
        task_list: main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTOTaskList = None,
    ):
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.stage_status = stage_status
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            self.task_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.stage_status is not None:
            result['StageStatus'] = self.stage_status

        if self.task_list is not None:
            result['TaskList'] = self.task_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('StageStatus') is not None:
            self.stage_status = m.get('StageStatus')

        if m.get('TaskList') is not None:
            temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTOTaskList()
            self.task_list = temp_model.from_map(m.get('TaskList'))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTOTaskList(DaraModel):
    def __init__(
        self,
        task_info_dto: List[main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTOTaskListTaskInfoDTO] = None,
    ):
        self.task_info_dto = task_info_dto

    def validate(self):
        if self.task_info_dto:
            for v1 in self.task_info_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskInfoDTO'] = []
        if self.task_info_dto is not None:
            for k1 in self.task_info_dto:
                result['TaskInfoDTO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_info_dto = []
        if m.get('TaskInfoDTO') is not None:
            for k1 in m.get('TaskInfoDTO'):
                temp_model = main_models.GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTOTaskListTaskInfoDTO()
                self.task_info_dto.append(temp_model.from_map(k1))

        return self

class GetChangeOrderInfoResponseBodyChangeOrderInfoPipelineInfoListPipelineInfoStageDetailListStageDetailDTOTaskListTaskInfoDTO(DaraModel):
    def __init__(
        self,
        retry_type: int = None,
        show_manual_ignorance: bool = None,
        task_error_code: str = None,
        task_error_ignorance: int = None,
        task_error_message: str = None,
        task_id: str = None,
        task_message: str = None,
        task_name: str = None,
        task_status: str = None,
    ):
        self.retry_type = retry_type
        self.show_manual_ignorance = show_manual_ignorance
        self.task_error_code = task_error_code
        self.task_error_ignorance = task_error_ignorance
        self.task_error_message = task_error_message
        self.task_id = task_id
        self.task_message = task_message
        self.task_name = task_name
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.retry_type is not None:
            result['RetryType'] = self.retry_type

        if self.show_manual_ignorance is not None:
            result['ShowManualIgnorance'] = self.show_manual_ignorance

        if self.task_error_code is not None:
            result['TaskErrorCode'] = self.task_error_code

        if self.task_error_ignorance is not None:
            result['TaskErrorIgnorance'] = self.task_error_ignorance

        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_message is not None:
            result['TaskMessage'] = self.task_message

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetryType') is not None:
            self.retry_type = m.get('RetryType')

        if m.get('ShowManualIgnorance') is not None:
            self.show_manual_ignorance = m.get('ShowManualIgnorance')

        if m.get('TaskErrorCode') is not None:
            self.task_error_code = m.get('TaskErrorCode')

        if m.get('TaskErrorIgnorance') is not None:
            self.task_error_ignorance = m.get('TaskErrorIgnorance')

        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

