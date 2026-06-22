# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

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
        can_try_post_paid_package: int = None,
        cspm_capacity: int = None,
        cspm_instance_capacity: int = None,
        highest_version: int = None,
        honeypot_capacity: int = None,
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
        sas_log: int = None,
        sas_screen: int = None,
        sdk_capacity: int = None,
        sls_capacity: int = None,
        threat_analysis_capacity: int = None,
        threat_analysis_flow: int = None,
        user_defined_alarms: int = None,
        version: int = None,
        vm_cores: int = None,
        vul_fix_capacity: int = None,
        web_lock: int = None,
        web_lock_auth_count: int = None,
    ):
        # The number of agentless detection quotas.
        # > Agentless detection is not available for purchase. You can ignore this field.
        self.agentless_capacity = agentless_capacity
        # Indicates whether pay-as-you-go purchasing is allowed.
        # 
        # - **0**: not allowed
        # - **1**: allowed.
        self.allow_partial_buy = allow_partial_buy
        # The anti-ransomware backup capacity. Unit: GB.
        self.anti_ransomware_capacity = anti_ransomware_capacity
        # The status of the anti-ransomware managed service. Valid values:
        # - **0**: not activated
        # - **1**: activated.
        self.anti_ransomware_service = anti_ransomware_service
        # Indicates whether the application whitelist is enabled. Valid values:
        # - **0**: disabled
        # - **2**: enabled.
        self.app_white_list = app_white_list
        # The number of application whitelist authorizations.
        # > One authorization allows you to apply an application whitelist policy to one server. After the application whitelist feature is enabled, the account has 20 authorizations by default.
        self.app_white_list_auth_count = app_white_list_auth_count
        # The number of purchased server authorization quotas.
        self.asset_level = asset_level
        # Indicates whether the pay-as-you-go trial plan can be activated. Valid values:
        # - **0**: not supported
        # - **1**: supported.
        self.can_try_post_paid_package = can_try_post_paid_package
        # The number of purchased Cloud Security Posture Management (CSPM) scans. Unit: times per month.
        self.cspm_capacity = cspm_capacity
        self.cspm_instance_capacity = cspm_instance_capacity
        # The highest purchased edition of Security Center. Valid values:
        # - **1**: Free Edition
        # - **3**: Enterprise Edition
        # - **5**: Pro Edition
        # - **6**: Anti-virus Edition
        # - **7**: Ultimate Edition
        # - **10**: Value-added services only
        # > If a single edition is purchased, this value indicates the corresponding edition. If multiple editions are purchased, this value indicates the highest edition among the purchased editions.
        self.highest_version = highest_version
        # The number of purchased honeypot authorization quotas.
        self.honeypot_capacity = honeypot_capacity
        self.hybrid_paid_module_switch_map = hybrid_paid_module_switch_map
        self.hybrid_paid_status = hybrid_paid_status
        self.hybrid_switch = hybrid_switch
        # The number of purchased image scan authorization quotas.
        self.image_scan_capacity = image_scan_capacity
        # The instance purchase type. Valid values:
        # - **0**: self-purchased
        # - **1**: allocated from a multi-account setup.
        self.instance_buy_type = instance_buy_type
        # The instance ID of the purchased Security Center instance.
        self.instance_id = instance_id
        # The AI digital human analysis traffic.
        self.intelligent_analysis_flow = intelligent_analysis_flow
        # Indicates whether the instance is the new Ultimate Edition.
        # 
        # - **true**: The instance is the latest version.
        # 
        # - **false**: The instance is not the latest version.
        self.is_new_container_version = is_new_container_version
        # Indicates whether the instance is the new Multi-version Edition.
        # 
        # - **true**: The instance is the latest multi-version.
        # 
        # - **false**: The instance is not the latest multi-version.
        self.is_new_multi_version = is_new_multi_version
        # Indicates whether the number of existing servers exceeds the maximum number of purchased authorizations. Valid values:
        # - **false**: The number does not exceed the limit.
        # - **true**: The number exceeds the limit.
        # 
        # >Notice: This parameter is deprecated. You can ignore it..
        self.is_over_balance = is_over_balance
        # Indicates whether pay-as-you-go billing is enabled. Valid values:
        # - **false**: disabled
        # - **true**: enabled.
        self.is_postpay = is_postpay
        # Indicates whether the current Security Center edition is a trial version. Valid values:
        # - **0**: not a trial version
        # - **1**: trial version.
        self.is_trial_version = is_trial_version
        # The end timestamp of the last trial of Security Center. Unit: milliseconds.
        self.last_trail_end_time = last_trail_end_time
        # The total number of authorizations when multiple editions are purchased.
        self.mvauth_count = mvauth_count
        # The total number of remaining authorizations when multiple editions are purchased.
        self.mvunused_auth_count = mvunused_auth_count
        # The higher protection edition between the subscription and pay-as-you-go host and container security services of Security Center when both are activated. Valid values:
        # - **1**: Free Edition
        # - **6**: Anti-virus Edition
        # - **5**: Premium Edition
        # - **3**: Enterprise Edition
        # - **7**: Ultimate Edition.
        self.merged_version = merged_version
        # The multi-version edition numbers and authorization usage.
        self.multi_version = multi_version
        self.new_post_paid_cspm = new_post_paid_cspm
        # Indicates whether the new version of Cloud Threat Detection and Response (CTDR) is enabled. The new version supports purchasing ingestion traffic and log storage capacity for Cloud Threat Detection and Response (CTDR). Valid values:
        # - **0**: disabled
        # - **1**: enabled.
        self.new_threat_analysis = new_threat_analysis
        # The number of AI digital human managed instances.
        self.onboarded_assets = onboarded_assets
        # The timestamp when the service was activated. Unit: milliseconds.
        self.open_time = open_time
        # The highest protection edition for bound assets when the pay-as-you-go host and container security service is activated. Valid values:
        # - **1**: Free Edition
        # - **3**: Enterprise Edition
        # - **5**: Pro Edition
        # - **6**: Anti-virus Edition
        # - **7**: Ultimate Edition.
        self.post_pay_host_version = post_pay_host_version
        # The instance ID of the pay-as-you-go instance.
        self.post_pay_instance_id = post_pay_instance_id
        # The status of pay-as-you-go module switches, in JSON string format. Valid values:
        # - Key:
        #   - **VUL**: vulnerability fix module
        #   - **CSPM**: Cloud Security Posture Management (CSPM) module
        #   - **AGENTLESS**: agentless detection module
        #   - **SERVERLESS**: serverless security module
        #   - **CTDR**: threat detection and response module
        #   - **POST_HOST**: host and container security module
        #   - **SDK**: malicious file detection SDK module
        #   - **RASP**: application protection module
        # - Value: 0 indicates disabled, 1 indicates enabled.
        self.post_pay_module_switch = post_pay_module_switch
        # The time when pay-as-you-go billing was activated.
        self.post_pay_open_time = post_pay_open_time
        # The instance status of the pay-as-you-go instance. Valid values:
        # - **1**: Normal.
        # - **2**: Suspended due to overdue payment.
        self.post_pay_status = post_pay_status
        # The number of purchased application protection quotas. Unit: per month.
        self.rasp_capacity = rasp_capacity
        # The UNIX timestamp when the Security Center instance expires. Unit: milliseconds.
        # > If you do not complete renewal within 7 days after the instance expires, your paid instance is downgraded to Free Edition. You can no longer use the features of the paid edition, and the Security Center configuration data and historical alerting data (such as DDoS alerts) become inaccessible. In this case, you must repurchase Security Center to enable the paid edition. For more information, see [Purchase Security Center](https://help.aliyun.com/document_detail/42308.html).
        self.release_time = release_time
        # The request ID.
        self.request_id = request_id
        # Indicates whether log analysis is purchased. Valid values:
        # - **0**: not purchased
        # - **1**: purchased.
        self.sas_log = sas_log
        # Indicates whether the security dashboard is purchased. Valid values:
        # - **0**: not purchased
        # - **1**: purchased.
        self.sas_screen = sas_screen
        # The number of malicious file detection SDK authorizations.
        self.sdk_capacity = sdk_capacity
        # The purchased log storage capacity. Unit: GB. Valid values: 0 to 200000.
        self.sls_capacity = sls_capacity
        # The purchased threat analysis capacity. Unit: GB.
        self.threat_analysis_capacity = threat_analysis_capacity
        # The purchased log ingestion traffic for threat detection and response. Unit: GB per day.
        self.threat_analysis_flow = threat_analysis_flow
        # Indicates whether the custom alerting feature is enabled. Valid values:
        # - **0**: disabled
        # - **2**: enabled.
        self.user_defined_alarms = user_defined_alarms
        # The purchased edition of Security Center. Valid values:  
        # - **1**: Free Edition 
        # - **3**: Enterprise Edition
        # - **5**: Pro Edition
        # - **6**: Anti-virus Edition    
        # - **7**: Ultimate Edition   
        # - **8**: Multi-version Edition   
        # - **10**: Value-added services only.
        self.version = version
        # The number of purchased authorized cores.
        self.vm_cores = vm_cores
        # The number of purchased vulnerability fixes. Unit: times per month.
        self.vul_fix_capacity = vul_fix_capacity
        # Indicates whether web tamper-proofing is enabled. Valid values:
        # - **0**: disabled
        # - **1**: enabled.
        self.web_lock = web_lock
        # The number of purchased web tamper-proofing authorizations. One authorization allows you to enable web tamper-proofing for one server. Valid values: 0 to N.
        # > N is the number of servers that you own.
        self.web_lock_auth_count = web_lock_auth_count

    def validate(self):
        pass

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

        if self.sas_log is not None:
            result['SasLog'] = self.sas_log

        if self.sas_screen is not None:
            result['SasScreen'] = self.sas_screen

        if self.sdk_capacity is not None:
            result['SdkCapacity'] = self.sdk_capacity

        if self.sls_capacity is not None:
            result['SlsCapacity'] = self.sls_capacity

        if self.threat_analysis_capacity is not None:
            result['ThreatAnalysisCapacity'] = self.threat_analysis_capacity

        if self.threat_analysis_flow is not None:
            result['ThreatAnalysisFlow'] = self.threat_analysis_flow

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

        if m.get('SasLog') is not None:
            self.sas_log = m.get('SasLog')

        if m.get('SasScreen') is not None:
            self.sas_screen = m.get('SasScreen')

        if m.get('SdkCapacity') is not None:
            self.sdk_capacity = m.get('SdkCapacity')

        if m.get('SlsCapacity') is not None:
            self.sls_capacity = m.get('SlsCapacity')

        if m.get('ThreatAnalysisCapacity') is not None:
            self.threat_analysis_capacity = m.get('ThreatAnalysisCapacity')

        if m.get('ThreatAnalysisFlow') is not None:
            self.threat_analysis_flow = m.get('ThreatAnalysisFlow')

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

