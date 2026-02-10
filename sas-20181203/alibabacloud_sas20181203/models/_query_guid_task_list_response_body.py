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
        # The list of beginner tasks.
        self.guide_task_config_list = guide_task_config_list
        # The request ID.
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
        # The information about the reward for a complete task.
        self.reward_data = reward_data
        # The security score that is increased after you complete the task.
        self.security_score = security_score
        # The status of the beginner task. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: in progress.
        # *   **2**: complete.
        self.status = status
        # The ID of the beginner task.
        self.task_id = task_id
        # The name of the task type. Valid values:
        # 
        # *   **guid_task_security_score_promote_video**: the task of viewing a video tutorial for beginners.
        # *   **guide_sub_task_config_defence_hbr**: the task of configuring anti-ransomware for servers.
        # *   **guide_sub_task_config_uni_defence_hbr**: the task of configuring anti-ransomware for databases.
        # *   **guid_task_log_analysis_config**: the task of configuring log analysis.
        # *   **guide_sub_task_web_lock_config**: the task of configuring web tamper proofing.
        # *   **guide_sub_task_config_anti_crack**: the task of configuring protection against brute-force attacks.
        # *   **guid_task_container_security_video**: the task of viewing the video on how to protect containers.
        # *   **guid_task_container_image_scan_config**: the task of configuring container image scan.
        # *   **guid_task_k8s_log_analysis_config**: the task of configuring threat detection on Kubernetes containers.
        # *   **guid_task_container_network**: the task of configuring container network visualization.
        # *   **guide_sub_task_config_add_collection**: the task of saving a console URL.
        # *   **guide_sub_task_vul_scan**: the task of scanning for vulnerabilities.
        # *   **guide_sub_task_virusKill**: the task of configuring virus detection and removal.
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
        # Indicates whether the reward is claimed. Valid values:
        # 
        # *   **1**: no.
        # *   **2**: yes.
        self.is_reward_taked = is_reward_taked
        # The name of the reward. Valid values:
        # 
        # *   **addTrialDay**: the days of trial use.
        # *   **addAntiRansomwareCapacity**: the anti-ransomware capacity.
        # *   **addImageScanAuthCount**: the quota for container image scan.
        # *   **addWebLockAuthCount**: the quota for web tamper proofing.
        # *   **addSlsCapacity**: the log storage capacity.
        self.reward = reward
        # The reward configuration. The value of this parameter is in the JSON format.
        # 
        # >  The key indicates the reward type, and the value indicates the number of rewards. Valid values of key:
        # 
        # *   **webLockAuthCount**: the quota for web tamper proofing.
        # *   **webLockAuthCount**: the anti-ransomware capacity. Unit: GB.
        # *   **slsCapacity**: the log storage capacity. Unit: GB.
        # *   **days**: the days of trial use.
        # *   **imageScanAuthCount**: the quota for container image scan.
        # *   **honeypotAuthCount**: the quota for cloud honeypot.
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

