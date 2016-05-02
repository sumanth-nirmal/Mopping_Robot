################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Each subdirectory must supply rules for building sources it contributes
Source/portable/CCS/ARM_CM4F/port.obj: ../Source/portable/CCS/ARM_CM4F/port.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"C:/ti/ccsv6/tools/compiler/ti-cgt-arm_5.2.5/bin/armcl" -mv7M4 --code_state=16 --float_support=FPv4SPD16 --abi=eabi -me --include_path="C:/ti/ccsv6/tools/compiler/ti-cgt-arm_5.2.5/include" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS/Source/portable/CCS/ARM_CM4F" --include_path="C:/D Drive/Start up/cleaner mob/MOPPING_BOT" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS/Source/include" -g --gcc --define=ccs="ccs" --define=TARGET_IS_TM4C123_RB1 --define=PART_TM4C123GH6PM --display_error_number --diag_warning=225 --diag_wrap=off --preproc_with_compile --preproc_dependency="Source/portable/CCS/ARM_CM4F/port.pp" --obj_directory="Source/portable/CCS/ARM_CM4F" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '

Source/portable/CCS/ARM_CM4F/portasm.obj: ../Source/portable/CCS/ARM_CM4F/portasm.asm $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"C:/ti/ccsv6/tools/compiler/ti-cgt-arm_5.2.5/bin/armcl" -mv7M4 --code_state=16 --float_support=FPv4SPD16 --abi=eabi -me --include_path="C:/ti/ccsv6/tools/compiler/ti-cgt-arm_5.2.5/include" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS/Source/portable/CCS/ARM_CM4F" --include_path="C:/D Drive/Start up/cleaner mob/MOPPING_BOT" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS/Source/include" -g --gcc --define=ccs="ccs" --define=TARGET_IS_TM4C123_RB1 --define=PART_TM4C123GH6PM --display_error_number --diag_warning=225 --diag_wrap=off --preproc_with_compile --preproc_dependency="Source/portable/CCS/ARM_CM4F/portasm.pp" --obj_directory="Source/portable/CCS/ARM_CM4F" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '


