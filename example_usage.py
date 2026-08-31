from client import DuplexTelephonyVoiceAgentTurnOrchestratorClient

def main():
    client = DuplexTelephonyVoiceAgentTurnOrchestratorClient()
    res = client.orchestrate_telephony_call('+12025550198', 'CUSTOMER_ONBOARDING_FOLLOWUP', 5)
    print('Telephony Voice Agent: ' + res['call_session_id'] + ' (' + str(res['call_duration_seconds']) + 's)')
    print('Turns: ' + str(res['turns_exchanged_count']) + ' | Interruption Latency: ' + str(res['speech_interruption_latency_ms']) + 'ms')
    print('Resolution Status: ' + res['intent_resolution_status'])
    print('Recording: ' + res['call_recording_wav_url'])
    print('Transcript: ' + res['call_transcript_json_url'])

if __name__ == '__main__':
    main()
