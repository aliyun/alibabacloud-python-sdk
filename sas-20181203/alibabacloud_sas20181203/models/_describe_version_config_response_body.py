# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVersionConfigResponseBody(DaraModel):
    def __init__(
        self,
        agentless_capacity: int = None,
        allow_partial_buy: int = None,
        anti_ransomware_capacity: int = None,
        anti_ransomware_service: int = None,
        app_white_list: int = None,
        app_white_list_auth_count: int = None,
        asset_level: int = None,
        buy_sas_edr: str = None,
        can_try_post_paid_package: int = None,
        cspm_capacity: int = None,
        cspm_instance_capacity: int = None,
        highest_version: int = None,
        honeypot_capacity: int = None,
        hybrid_paid_gray_status: str = None,
        hybrid_paid_module_switch_map: int = None,
        hybrid_paid_status: int = None,
        hybrid_switch: int = None,
        image_scan_capacity: int = None,
        instance_buy_type: int = None,
        instance_id: str = None,
        intelligent_analysis_flow: int = None,
        is_new_container_version: bool = None,
        is_new_multi_version: bool = None,
        is_over_balance: bool = None,
        is_postpay: bool = None,
        is_trial_version: int = None,
        last_trail_end_time: int = None,
        mvauth_count: int = None,
        mvunused_auth_count: int = None,
        merged_version: int = None,
        multi_version: str = None,
        new_post_paid_cspm: int = None,
        new_threat_analysis: int = None,
        onboarded_assets: int = None,
        open_time: int = None,
        post_pay_host_version: int = None,
        post_pay_instance_id: str = None,
        post_pay_module_switch: str = None,
        post_pay_open_time: int = None,
        post_pay_status: int = None,
        rasp_capacity: int = None,
        release_time: int = None,
        request_id: str = None,
        sas_edr_client_auth_count: str = None,
        sas_edr_post_paid_instance_id: str = None,
        sas_edr_pre_paid_instance_id: str = None,
        sas_edr_pre_paid_instance_status: str = None,
        sas_edr_version: str = None,
        sas_log: int = None,
        sas_screen: int = None,
        sdk_ai_post_paid_gray: int = None,
        sdk_capacity: int = None,
        sls_capacity: int = None,
        threat_analysis_capacity: int = None,
        threat_analysis_flow: int = None,
        trial_module_list: List[main_models.DescribeVersionConfigResponseBodyTrialModuleList] = None,
        trial_version: int = None,
        user_defined_alarms: int = None,
        version: int = None,
        vm_cores: int = None,
        vul_fix_capacity: int = None,
        web_lock: int = None,
        web_lock_auth_count: int = None,
    ):
        # The number of agentless detections.
        # > Agentless detection is not currently available for purchase. You do not need to pay attention to this field.
        self.agentless_capacity = agentless_capacity
        # Indicates whether pay-as-you-go purchasing is allowed. Valid values:
        # 
        # - **0**: Not allowed.
        # - **1**: Allowed.
        self.allow_partial_buy = allow_partial_buy
        # The anti-ransomware backup capacity. Unit: GB.
        self.anti_ransomware_capacity = anti_ransomware_capacity
        # The anti-ransomware managed service. Valid values:
        # - **0**: Not enabled.
        # - **1**: Enabled.
        self.anti_ransomware_service = anti_ransomware_service
        # Indicates whether the application whitelist is enabled. Valid values:
        # - **0**: Not enabled.
        # - **2**: Enabled.
        self.app_white_list = app_white_list
        # The number of application whitelist authorizations.
        # > One authorization can apply an application whitelist policy to one server. After the application whitelist feature is enabled, the account has 20 authorizations by default.
        self.app_white_list_auth_count = app_white_list_auth_count
        # The number of purchased server authorizations.
        self.asset_level = asset_level
        # Indicates whether EDR is purchased.
        self.buy_sas_edr = buy_sas_edr
        # Indicates whether the post-paid trial package can be activated. Valid values:
        # - **0**: Not supported.
        # - **1**: Supported.
        self.can_try_post_paid_package = can_try_post_paid_package
        # The number of purchased cloud platform configuration check scans. Unit: times/month.
        self.cspm_capacity = cspm_capacity
        # The AI digital human analysis traffic.
        self.cspm_instance_capacity = cspm_instance_capacity
        # The highest purchased Security Center version. Valid values:
        # - **1**: Free edition.
        # - **3**: Enterprise edition.
        # - **5**: Advanced edition.
        # - **6**: Anti-virus edition.
        # - **7**: Ultimate edition.
        # - **10**: Value-added services only.
        # > If a single version is purchased, this value indicates the corresponding version. If multiple versions are purchased, this value indicates the highest version among the purchased Security Center versions.
        self.highest_version = highest_version
        # The number of purchased honeypot authorizations.
        self.honeypot_capacity = honeypot_capacity
        # The grayscale module for elastic billing.
        self.hybrid_paid_gray_status = hybrid_paid_gray_status
        # The AI digital human analysis traffic.
        self.hybrid_paid_module_switch_map = hybrid_paid_module_switch_map
        # The elastic billing switch status.
        self.hybrid_paid_status = hybrid_paid_status
        # The AI digital human analysis traffic.
        self.hybrid_switch = hybrid_switch
        # The number of purchased image scan authorizations.
        self.image_scan_capacity = image_scan_capacity
        # The instance purchase type. Valid values:
        # - **0**: Self-purchased.
        # - **1**: Allocated by multi-account management.
        self.instance_buy_type = instance_buy_type
        # The ID of the purchased Security Center instance.
        self.instance_id = instance_id
        # The AI digital human analysis traffic.
        self.intelligent_analysis_flow = intelligent_analysis_flow
        # Indicates whether this is the new Ultimate edition. Valid values:
        # 
        # - **true**: The latest version.
        # 
        # - **false**: Not the latest version.
        self.is_new_container_version = is_new_container_version
        # Indicates whether this is the new multi-version edition. Valid values:
        # 
        # - **true**: The latest multi-version edition.
        # 
        # - **false**: Not the latest multi-version edition.
        self.is_new_multi_version = is_new_multi_version
        # Indicates whether the current number of servers exceeds the maximum number of purchased authorizations. Valid values:
        # - **false**: Not exceeded.
        # - **true**: Exceeded.
        # 
        # >Notice: This parameter is deprecated. You do not need to pay attention to it.
        self.is_over_balance = is_over_balance
        # Indicates whether pay-as-you-go billing is enabled. Valid values:
        # - **false**: Not enabled.
        # - **true**: Enabled.
        self.is_postpay = is_postpay
        # Indicates whether the current Security Center version is a trial version. Valid values:
        # - **0**: Not a trial version.
        # - **1**: Trial version.
        self.is_trial_version = is_trial_version
        # The end timestamp of the last trial of Security Center. Unit: milliseconds.
        self.last_trail_end_time = last_trail_end_time
        # The total number of authorizations when multiple versions are purchased.
        self.mvauth_count = mvauth_count
        # The total number of remaining authorizations when multiple versions are purchased.
        self.mvunused_auth_count = mvunused_auth_count
        # The higher protection version between the subscription and pay-as-you-go Security Center host and container security services when both are enabled. Valid values:
        # - **1**: Free edition.
        # - **6**: Anti-virus edition.
        # - **5**: Advanced edition.
        # - **3**: Enterprise edition.
        # - **7**: Ultimate edition.
        self.merged_version = merged_version
        # The multi-version number and authorization usage information.
        self.multi_version = multi_version
        # The AI digital human analysis traffic.
        self.new_post_paid_cspm = new_post_paid_cspm
        # Indicates whether the new threat analysis and response service is enabled. The new threat analysis and response service supports purchasing ingestion traffic and log storage capacity. Valid values:
        # - **0**: No.
        # - **1**: Yes.
        self.new_threat_analysis = new_threat_analysis
        # The AI digital human managed instances.
        self.onboarded_assets = onboarded_assets
        # The timestamp when the service was activated. Unit: milliseconds.
        self.open_time = open_time
        # The highest protection version bound to assets when the host and container security pay-as-you-go service is enabled. Valid values:
        # - **1**: Free edition.
        # - **3**: Enterprise edition.
        # - **5**: Advanced edition.
        # - **6**: Anti-virus edition.
        # - **7**: Ultimate edition.
        self.post_pay_host_version = post_pay_host_version
        # The ID of the pay-as-you-go instance.
        self.post_pay_instance_id = post_pay_instance_id
        # The switch status of pay-as-you-go modules in JSON string format. Valid values:
        # - Key:
        #   - **VUL**: Vulnerability fix module.
        #   - **CSPM**: Cloud security posture management module.
        #   - **AGENTLESS**: Agentless detection module.
        #   - **SERVERLESS**: Serverless security module.
        #   - **CTDR**: Threat analysis and response module.
        #   - **POST_HOST**: Host and container security module.
        #   - **SDK**: Malicious file detection SDK module.
        #   - **RASP**: Application protection module.
        # - Value: 0 indicates disabled, and 1 indicates enabled.
        self.post_pay_module_switch = post_pay_module_switch
        # The time when pay-as-you-go billing was activated.
        self.post_pay_open_time = post_pay_open_time
        # The status of the pay-as-you-go instance. Valid values:
        # - **1**: Normal.
        # - **2**: Suspended due to overdue payment.
        self.post_pay_status = post_pay_status
        # The number of purchased application protection instances. Unit: instances/month.
        self.rasp_capacity = rasp_capacity
        # The expiration timestamp of the Security Center instance. Unit: milliseconds.
        # > If you do not renew the service within 7 days after it expires, your paid instance is downgraded to the free edition. You can no longer use the features of the paid edition, and your Security Center configuration data and historical alert data (such as DDoS alerts) become inaccessible. In this case, you must repurchase to enable the paid Security Center service. For more information, see [Purchase Security Center](https://help.aliyun.com/document_detail/42308.html).
        self.release_time = release_time
        # The request ID.
        self.request_id = request_id
        # The number of machines purchased for EDR.
        self.sas_edr_client_auth_count = sas_edr_client_auth_count
        # The pay-as-you-go instance ID of EDR.
        self.sas_edr_post_paid_instance_id = sas_edr_post_paid_instance_id
        # The subscription instance ID of EDR.
        self.sas_edr_pre_paid_instance_id = sas_edr_pre_paid_instance_id
        # The EDR subscription instance status.
        self.sas_edr_pre_paid_instance_status = sas_edr_pre_paid_instance_status
        # The purchased EDR version.
        self.sas_edr_version = sas_edr_version
        # Indicates whether log analysis is purchased. Valid values:
        # - **0**: Not purchased.
        # - **1**: Purchased.
        self.sas_log = sas_log
        # Indicates whether the security dashboard is purchased. Valid values:
        # - **0**: Not purchased.
        # - **1**: Purchased.
        self.sas_screen = sas_screen
        self.sdk_ai_post_paid_gray = sdk_ai_post_paid_gray
        # The number of malicious file detection SDK authorizations.
        self.sdk_capacity = sdk_capacity
        # The purchased log storage capacity. Unit: GB. Valid values: 0 to 200000.
        self.sls_capacity = sls_capacity
        # The purchased threat analysis capacity. Unit: GB.
        self.threat_analysis_capacity = threat_analysis_capacity
        # The purchased threat analysis and response log ingestion traffic. Unit: GB/day.
        self.threat_analysis_flow = threat_analysis_flow
        # The list of trial sub-modules.
        self.trial_module_list = trial_module_list
        # The trial version.
        self.trial_version = trial_version
        # Indicates whether the custom alert feature is enabled. Valid values:
        # - **0**: Not enabled.
        # - **2**: Enabled.
        self.user_defined_alarms = user_defined_alarms
        # The purchased Security Center version. Valid values:  
        # - **1**: Free edition. 
        # - **3**: Enterprise edition.
        # - **5**: Advanced edition.
        # - **6**: Anti-virus edition.    
        # - **7**: Ultimate edition.   
        # - **8**: Multi-version edition.   
        # - **10**: Value-added services only.
        self.version = version
        # The number of purchased authorized cores.
        self.vm_cores = vm_cores
        # The number of purchased vulnerability fixes. Unit: times/month.
        self.vul_fix_capacity = vul_fix_capacity
        # Indicates whether the tamper-proofing service is enabled. Valid values:
        # - **0**: Not enabled.
        # - **1**: Enabled.
        self.web_lock = web_lock
        # The number of purchased tamper-proofing authorizations. One authorization can enable tamper-proofing protection for one server. Valid values: 0 to N.
        # > N is the number of servers you own.
        self.web_lock_auth_count = web_lock_auth_count

    def validate(self):
        if self.trial_module_list:
            for v1 in self.trial_module_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentless_capacity is not None:
            result['AgentlessCapacity'] = self.agentless_capacity

        if self.allow_partial_buy is not None:
            result['AllowPartialBuy'] = self.allow_partial_buy

        if self.anti_ransomware_capacity is not None:
            result['AntiRansomwareCapacity'] = self.anti_ransomware_capacity

        if self.anti_ransomware_service is not None:
            result['AntiRansomwareService'] = self.anti_ransomware_service

        if self.app_white_list is not None:
            result['AppWhiteList'] = self.app_white_list

        if self.app_white_list_auth_count is not None:
            result['AppWhiteListAuthCount'] = self.app_white_list_auth_count

        if self.asset_level is not None:
            result['AssetLevel'] = self.asset_level

        if self.buy_sas_edr is not None:
            result['BuySasEdr'] = self.buy_sas_edr

        if self.can_try_post_paid_package is not None:
            result['CanTryPostPaidPackage'] = self.can_try_post_paid_package

        if self.cspm_capacity is not None:
            result['CspmCapacity'] = self.cspm_capacity

        if self.cspm_instance_capacity is not None:
            result['CspmInstanceCapacity'] = self.cspm_instance_capacity

        if self.highest_version is not None:
            result['HighestVersion'] = self.highest_version

        if self.honeypot_capacity is not None:
            result['HoneypotCapacity'] = self.honeypot_capacity

        if self.hybrid_paid_gray_status is not None:
            result['HybridPaidGrayStatus'] = self.hybrid_paid_gray_status

        if self.hybrid_paid_module_switch_map is not None:
            result['HybridPaidModuleSwitchMap'] = self.hybrid_paid_module_switch_map

        if self.hybrid_paid_status is not None:
            result['HybridPaidStatus'] = self.hybrid_paid_status

        if self.hybrid_switch is not None:
            result['HybridSwitch'] = self.hybrid_switch

        if self.image_scan_capacity is not None:
            result['ImageScanCapacity'] = self.image_scan_capacity

        if self.instance_buy_type is not None:
            result['InstanceBuyType'] = self.instance_buy_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intelligent_analysis_flow is not None:
            result['IntelligentAnalysisFlow'] = self.intelligent_analysis_flow

        if self.is_new_container_version is not None:
            result['IsNewContainerVersion'] = self.is_new_container_version

        if self.is_new_multi_version is not None:
            result['IsNewMultiVersion'] = self.is_new_multi_version

        if self.is_over_balance is not None:
            result['IsOverBalance'] = self.is_over_balance

        if self.is_postpay is not None:
            result['IsPostpay'] = self.is_postpay

        if self.is_trial_version is not None:
            result['IsTrialVersion'] = self.is_trial_version

        if self.last_trail_end_time is not None:
            result['LastTrailEndTime'] = self.last_trail_end_time

        if self.mvauth_count is not None:
            result['MVAuthCount'] = self.mvauth_count

        if self.mvunused_auth_count is not None:
            result['MVUnusedAuthCount'] = self.mvunused_auth_count

        if self.merged_version is not None:
            result['MergedVersion'] = self.merged_version

        if self.multi_version is not None:
            result['MultiVersion'] = self.multi_version

        if self.new_post_paid_cspm is not None:
            result['NewPostPaidCspm'] = self.new_post_paid_cspm

        if self.new_threat_analysis is not None:
            result['NewThreatAnalysis'] = self.new_threat_analysis

        if self.onboarded_assets is not None:
            result['OnboardedAssets'] = self.onboarded_assets

        if self.open_time is not None:
            result['OpenTime'] = self.open_time

        if self.post_pay_host_version is not None:
            result['PostPayHostVersion'] = self.post_pay_host_version

        if self.post_pay_instance_id is not None:
            result['PostPayInstanceId'] = self.post_pay_instance_id

        if self.post_pay_module_switch is not None:
            result['PostPayModuleSwitch'] = self.post_pay_module_switch

        if self.post_pay_open_time is not None:
            result['PostPayOpenTime'] = self.post_pay_open_time

        if self.post_pay_status is not None:
            result['PostPayStatus'] = self.post_pay_status

        if self.rasp_capacity is not None:
            result['RaspCapacity'] = self.rasp_capacity

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sas_edr_client_auth_count is not None:
            result['SasEdrClientAuthCount'] = self.sas_edr_client_auth_count

        if self.sas_edr_post_paid_instance_id is not None:
            result['SasEdrPostPaidInstanceId'] = self.sas_edr_post_paid_instance_id

        if self.sas_edr_pre_paid_instance_id is not None:
            result['SasEdrPrePaidInstanceId'] = self.sas_edr_pre_paid_instance_id

        if self.sas_edr_pre_paid_instance_status is not None:
            result['SasEdrPrePaidInstanceStatus'] = self.sas_edr_pre_paid_instance_status

        if self.sas_edr_version is not None:
            result['SasEdrVersion'] = self.sas_edr_version

        if self.sas_log is not None:
            result['SasLog'] = self.sas_log

        if self.sas_screen is not None:
            result['SasScreen'] = self.sas_screen

        if self.sdk_ai_post_paid_gray is not None:
            result['SdkAiPostPaidGray'] = self.sdk_ai_post_paid_gray

        if self.sdk_capacity is not None:
            result['SdkCapacity'] = self.sdk_capacity

        if self.sls_capacity is not None:
            result['SlsCapacity'] = self.sls_capacity

        if self.threat_analysis_capacity is not None:
            result['ThreatAnalysisCapacity'] = self.threat_analysis_capacity

        if self.threat_analysis_flow is not None:
            result['ThreatAnalysisFlow'] = self.threat_analysis_flow

        result['TrialModuleList'] = []
        if self.trial_module_list is not None:
            for k1 in self.trial_module_list:
                result['TrialModuleList'].append(k1.to_map() if k1 else None)

        if self.trial_version is not None:
            result['TrialVersion'] = self.trial_version

        if self.user_defined_alarms is not None:
            result['UserDefinedAlarms'] = self.user_defined_alarms

        if self.version is not None:
            result['Version'] = self.version

        if self.vm_cores is not None:
            result['VmCores'] = self.vm_cores

        if self.vul_fix_capacity is not None:
            result['VulFixCapacity'] = self.vul_fix_capacity

        if self.web_lock is not None:
            result['WebLock'] = self.web_lock

        if self.web_lock_auth_count is not None:
            result['WebLockAuthCount'] = self.web_lock_auth_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentlessCapacity') is not None:
            self.agentless_capacity = m.get('AgentlessCapacity')

        if m.get('AllowPartialBuy') is not None:
            self.allow_partial_buy = m.get('AllowPartialBuy')

        if m.get('AntiRansomwareCapacity') is not None:
            self.anti_ransomware_capacity = m.get('AntiRansomwareCapacity')

        if m.get('AntiRansomwareService') is not None:
            self.anti_ransomware_service = m.get('AntiRansomwareService')

        if m.get('AppWhiteList') is not None:
            self.app_white_list = m.get('AppWhiteList')

        if m.get('AppWhiteListAuthCount') is not None:
            self.app_white_list_auth_count = m.get('AppWhiteListAuthCount')

        if m.get('AssetLevel') is not None:
            self.asset_level = m.get('AssetLevel')

        if m.get('BuySasEdr') is not None:
            self.buy_sas_edr = m.get('BuySasEdr')

        if m.get('CanTryPostPaidPackage') is not None:
            self.can_try_post_paid_package = m.get('CanTryPostPaidPackage')

        if m.get('CspmCapacity') is not None:
            self.cspm_capacity = m.get('CspmCapacity')

        if m.get('CspmInstanceCapacity') is not None:
            self.cspm_instance_capacity = m.get('CspmInstanceCapacity')

        if m.get('HighestVersion') is not None:
            self.highest_version = m.get('HighestVersion')

        if m.get('HoneypotCapacity') is not None:
            self.honeypot_capacity = m.get('HoneypotCapacity')

        if m.get('HybridPaidGrayStatus') is not None:
            self.hybrid_paid_gray_status = m.get('HybridPaidGrayStatus')

        if m.get('HybridPaidModuleSwitchMap') is not None:
            self.hybrid_paid_module_switch_map = m.get('HybridPaidModuleSwitchMap')

        if m.get('HybridPaidStatus') is not None:
            self.hybrid_paid_status = m.get('HybridPaidStatus')

        if m.get('HybridSwitch') is not None:
            self.hybrid_switch = m.get('HybridSwitch')

        if m.get('ImageScanCapacity') is not None:
            self.image_scan_capacity = m.get('ImageScanCapacity')

        if m.get('InstanceBuyType') is not None:
            self.instance_buy_type = m.get('InstanceBuyType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntelligentAnalysisFlow') is not None:
            self.intelligent_analysis_flow = m.get('IntelligentAnalysisFlow')

        if m.get('IsNewContainerVersion') is not None:
            self.is_new_container_version = m.get('IsNewContainerVersion')

        if m.get('IsNewMultiVersion') is not None:
            self.is_new_multi_version = m.get('IsNewMultiVersion')

        if m.get('IsOverBalance') is not None:
            self.is_over_balance = m.get('IsOverBalance')

        if m.get('IsPostpay') is not None:
            self.is_postpay = m.get('IsPostpay')

        if m.get('IsTrialVersion') is not None:
            self.is_trial_version = m.get('IsTrialVersion')

        if m.get('LastTrailEndTime') is not None:
            self.last_trail_end_time = m.get('LastTrailEndTime')

        if m.get('MVAuthCount') is not None:
            self.mvauth_count = m.get('MVAuthCount')

        if m.get('MVUnusedAuthCount') is not None:
            self.mvunused_auth_count = m.get('MVUnusedAuthCount')

        if m.get('MergedVersion') is not None:
            self.merged_version = m.get('MergedVersion')

        if m.get('MultiVersion') is not None:
            self.multi_version = m.get('MultiVersion')

        if m.get('NewPostPaidCspm') is not None:
            self.new_post_paid_cspm = m.get('NewPostPaidCspm')

        if m.get('NewThreatAnalysis') is not None:
            self.new_threat_analysis = m.get('NewThreatAnalysis')

        if m.get('OnboardedAssets') is not None:
            self.onboarded_assets = m.get('OnboardedAssets')

        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')

        if m.get('PostPayHostVersion') is not None:
            self.post_pay_host_version = m.get('PostPayHostVersion')

        if m.get('PostPayInstanceId') is not None:
            self.post_pay_instance_id = m.get('PostPayInstanceId')

        if m.get('PostPayModuleSwitch') is not None:
            self.post_pay_module_switch = m.get('PostPayModuleSwitch')

        if m.get('PostPayOpenTime') is not None:
            self.post_pay_open_time = m.get('PostPayOpenTime')

        if m.get('PostPayStatus') is not None:
            self.post_pay_status = m.get('PostPayStatus')

        if m.get('RaspCapacity') is not None:
            self.rasp_capacity = m.get('RaspCapacity')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SasEdrClientAuthCount') is not None:
            self.sas_edr_client_auth_count = m.get('SasEdrClientAuthCount')

        if m.get('SasEdrPostPaidInstanceId') is not None:
            self.sas_edr_post_paid_instance_id = m.get('SasEdrPostPaidInstanceId')

        if m.get('SasEdrPrePaidInstanceId') is not None:
            self.sas_edr_pre_paid_instance_id = m.get('SasEdrPrePaidInstanceId')

        if m.get('SasEdrPrePaidInstanceStatus') is not None:
            self.sas_edr_pre_paid_instance_status = m.get('SasEdrPrePaidInstanceStatus')

        if m.get('SasEdrVersion') is not None:
            self.sas_edr_version = m.get('SasEdrVersion')

        if m.get('SasLog') is not None:
            self.sas_log = m.get('SasLog')

        if m.get('SasScreen') is not None:
            self.sas_screen = m.get('SasScreen')

        if m.get('SdkAiPostPaidGray') is not None:
            self.sdk_ai_post_paid_gray = m.get('SdkAiPostPaidGray')

        if m.get('SdkCapacity') is not None:
            self.sdk_capacity = m.get('SdkCapacity')

        if m.get('SlsCapacity') is not None:
            self.sls_capacity = m.get('SlsCapacity')

        if m.get('ThreatAnalysisCapacity') is not None:
            self.threat_analysis_capacity = m.get('ThreatAnalysisCapacity')

        if m.get('ThreatAnalysisFlow') is not None:
            self.threat_analysis_flow = m.get('ThreatAnalysisFlow')

        self.trial_module_list = []
        if m.get('TrialModuleList') is not None:
            for k1 in m.get('TrialModuleList'):
                temp_model = main_models.DescribeVersionConfigResponseBodyTrialModuleList()
                self.trial_module_list.append(temp_model.from_map(k1))

        if m.get('TrialVersion') is not None:
            self.trial_version = m.get('TrialVersion')

        if m.get('UserDefinedAlarms') is not None:
            self.user_defined_alarms = m.get('UserDefinedAlarms')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VmCores') is not None:
            self.vm_cores = m.get('VmCores')

        if m.get('VulFixCapacity') is not None:
            self.vul_fix_capacity = m.get('VulFixCapacity')

        if m.get('WebLock') is not None:
            self.web_lock = m.get('WebLock')

        if m.get('WebLockAuthCount') is not None:
            self.web_lock_auth_count = m.get('WebLockAuthCount')

        return self

class DescribeVersionConfigResponseBodyTrialModuleList(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the trial sub-module.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

