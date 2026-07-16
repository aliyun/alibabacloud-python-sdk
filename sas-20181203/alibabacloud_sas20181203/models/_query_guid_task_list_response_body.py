# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class QueryGuidTaskListResponseBody(DaraModel):
    def __init__(
        self,
        guide_task_config_list: List[main_models.QueryGuidTaskListResponseBodyGuideTaskConfigList] = None,
        request_id: str = None,
    ):
        # The list of beginner task information.
        self.guide_task_config_list = guide_task_config_list
        # The request ID. Alibaba Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.guide_task_config_list:
            for v1 in self.guide_task_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GuideTaskConfigList'] = []
        if self.guide_task_config_list is not None:
            for k1 in self.guide_task_config_list:
                result['GuideTaskConfigList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.guide_task_config_list = []
        if m.get('GuideTaskConfigList') is not None:
            for k1 in m.get('GuideTaskConfigList'):
                temp_model = main_models.QueryGuidTaskListResponseBodyGuideTaskConfigList()
                self.guide_task_config_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryGuidTaskListResponseBodyGuideTaskConfigList(DaraModel):
    def __init__(
        self,
        reward_data: main_models.QueryGuidTaskListResponseBodyGuideTaskConfigListRewardData = None,
        security_score: int = None,
        status: int = None,
        task_id: int = None,
        task_type_name: str = None,
    ):
        # The reward information for task completion.
        self.reward_data = reward_data
        # The security score increase that can be gained by completing this task.
        self.security_score = security_score
        # The task status. Valid values:
        # - **0**: Closed.
        # - **1**: In progress.
        # - **2**: Completed.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The node name. Valid values:
        # 
        # - **guid_task_security_score_promote_video**: the node of watching the beginner quick start video
        # - **guide_sub_task_config_defence_hbr**: the anti-ransomware configuration node for servers
        # - **guide_sub_task_config_uni_defence_hbr**: the anti-ransomware configuration node for databases
        # - **guid_task_log_analysis_config**: the log analysis node
        # - **guide_sub_task_web_lock_config**: the web tamper-proofing node
        # - **guide_sub_task_config_anti_crack**: the anti-brute-force attacks node
        # - **guid_task_container_security_video**: the container security video node
        # - **guid_task_container_image_scan_config**: the container image scan node
        # - **guid_task_k8s_log_analysis_config**: the Kubernetes threat detection node
        # - **guid_task_container_network**: the container visualization node
        # - **guide_sub_task_config_add_collection**: the node of adding the console to favorites
        # - **guide_sub_task_vul_scan**: the vulnerability scanning node
        # - **guide_sub_task_virusKill**: the virus scan node.
        self.task_type_name = task_type_name

    def validate(self):
        if self.reward_data:
            self.reward_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reward_data is not None:
            result['RewardData'] = self.reward_data.to_map()

        if self.security_score is not None:
            result['SecurityScore'] = self.security_score

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type_name is not None:
            result['TaskTypeName'] = self.task_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RewardData') is not None:
            temp_model = main_models.QueryGuidTaskListResponseBodyGuideTaskConfigListRewardData()
            self.reward_data = temp_model.from_map(m.get('RewardData'))

        if m.get('SecurityScore') is not None:
            self.security_score = m.get('SecurityScore')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskTypeName') is not None:
            self.task_type_name = m.get('TaskTypeName')

        return self

class QueryGuidTaskListResponseBodyGuideTaskConfigListRewardData(DaraModel):
    def __init__(
        self,
        is_reward_taked: str = None,
        reward: str = None,
        reward_config: str = None,
    ):
        # The claim status. Valid values:
        # - **1**: Not claimed.
        # - **2**: Claimed.
        self.is_reward_taked = is_reward_taked
        # The reward name. Valid values:
        # - **addTrialDay**: trial days reward
        # - **addAntiRansomwareCapacity**: anti-ransomware capacity reward
        # - **addImageScanAuthCount**: image scan authorization quota reward
        # - **addWebLockAuthCount**: web tamper-proofing authorization quota reward
        # - **addSlsCapacity**: log analysis storage capacity reward.
        self.reward = reward
        # The reward configuration information. This parameter is in JSON format.
        # > The key in the JSON object indicates the reward content, and the value indicates the reward amount. Valid values of the key:
        # - **webLockAuthCount**: the web tamper-proofing authorization quota
        # - **ransomwareCapacity**: the anti-ransomware capacity, in GB
        # - **slsCapacity**: the log analysis capacity, in GB
        # - **days**: the number of usage days
        # - **imageScanAuthCount**: the image scan authorization quota
        # - **honeypotAuthCount**: the cloud honeypot authorization quota.
        self.reward_config = reward_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_reward_taked is not None:
            result['IsRewardTaked'] = self.is_reward_taked

        if self.reward is not None:
            result['Reward'] = self.reward

        if self.reward_config is not None:
            result['RewardConfig'] = self.reward_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsRewardTaked') is not None:
            self.is_reward_taked = m.get('IsRewardTaked')

        if m.get('Reward') is not None:
            self.reward = m.get('Reward')

        if m.get('RewardConfig') is not None:
            self.reward_config = m.get('RewardConfig')

        return self

