# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartUserAppAsyncEnhanceInMsaRequest(DaraModel):
    def __init__(
        self,
        apk_protector: bool = None,
        app_id: str = None,
        assets_file_list: str = None,
        classes: str = None,
        dalvik_debugger: int = None,
        emulator_environment: int = None,
        id: int = None,
        java_hook: int = None,
        memory_dump: int = None,
        native_debugger: int = None,
        native_hook: int = None,
        new_shield_config: str = None,
        package_tampered: int = None,
        root: int = None,
        run_mode: str = None,
        so_file_list: str = None,
        task_type: str = None,
        tenant_id: str = None,
        total_switch: bool = None,
        use_ashield: bool = None,
        use_yshield: bool = None,
        workspace_id: str = None,
    ):
        self.apk_protector = apk_protector
        # This parameter is required.
        self.app_id = app_id
        self.assets_file_list = assets_file_list
        self.classes = classes
        self.dalvik_debugger = dalvik_debugger
        self.emulator_environment = emulator_environment
        # This parameter is required.
        self.id = id
        self.java_hook = java_hook
        self.memory_dump = memory_dump
        self.native_debugger = native_debugger
        self.native_hook = native_hook
        self.new_shield_config = new_shield_config
        self.package_tampered = package_tampered
        self.root = root
        self.run_mode = run_mode
        self.so_file_list = so_file_list
        self.task_type = task_type
        # This parameter is required.
        self.tenant_id = tenant_id
        self.total_switch = total_switch
        self.use_ashield = use_ashield
        self.use_yshield = use_yshield
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apk_protector is not None:
            result['ApkProtector'] = self.apk_protector

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.assets_file_list is not None:
            result['AssetsFileList'] = self.assets_file_list

        if self.classes is not None:
            result['Classes'] = self.classes

        if self.dalvik_debugger is not None:
            result['DalvikDebugger'] = self.dalvik_debugger

        if self.emulator_environment is not None:
            result['EmulatorEnvironment'] = self.emulator_environment

        if self.id is not None:
            result['Id'] = self.id

        if self.java_hook is not None:
            result['JavaHook'] = self.java_hook

        if self.memory_dump is not None:
            result['MemoryDump'] = self.memory_dump

        if self.native_debugger is not None:
            result['NativeDebugger'] = self.native_debugger

        if self.native_hook is not None:
            result['NativeHook'] = self.native_hook

        if self.new_shield_config is not None:
            result['NewShieldConfig'] = self.new_shield_config

        if self.package_tampered is not None:
            result['PackageTampered'] = self.package_tampered

        if self.root is not None:
            result['Root'] = self.root

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.so_file_list is not None:
            result['SoFileList'] = self.so_file_list

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.total_switch is not None:
            result['TotalSwitch'] = self.total_switch

        if self.use_ashield is not None:
            result['UseAShield'] = self.use_ashield

        if self.use_yshield is not None:
            result['UseYShield'] = self.use_yshield

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkProtector') is not None:
            self.apk_protector = m.get('ApkProtector')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AssetsFileList') is not None:
            self.assets_file_list = m.get('AssetsFileList')

        if m.get('Classes') is not None:
            self.classes = m.get('Classes')

        if m.get('DalvikDebugger') is not None:
            self.dalvik_debugger = m.get('DalvikDebugger')

        if m.get('EmulatorEnvironment') is not None:
            self.emulator_environment = m.get('EmulatorEnvironment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JavaHook') is not None:
            self.java_hook = m.get('JavaHook')

        if m.get('MemoryDump') is not None:
            self.memory_dump = m.get('MemoryDump')

        if m.get('NativeDebugger') is not None:
            self.native_debugger = m.get('NativeDebugger')

        if m.get('NativeHook') is not None:
            self.native_hook = m.get('NativeHook')

        if m.get('NewShieldConfig') is not None:
            self.new_shield_config = m.get('NewShieldConfig')

        if m.get('PackageTampered') is not None:
            self.package_tampered = m.get('PackageTampered')

        if m.get('Root') is not None:
            self.root = m.get('Root')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('SoFileList') is not None:
            self.so_file_list = m.get('SoFileList')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TotalSwitch') is not None:
            self.total_switch = m.get('TotalSwitch')

        if m.get('UseAShield') is not None:
            self.use_ashield = m.get('UseAShield')

        if m.get('UseYShield') is not None:
            self.use_yshield = m.get('UseYShield')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

