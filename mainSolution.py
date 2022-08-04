import api, coh, overheads, profit_loss

def main():
    forex = api.api_function()
    overheads_max = overheads.overhead_functions(forex)
    pnl_loss = profit_loss.profitloss_function(forex)
    coh_loss = coh.coh_function(forex)

    with open('summary_report.txt', 'w') as f:
        f.write(f'[REAL_TIME_CURRENCY_CONVERSION_RATE] USD1 = SGD{forex}\n')
        f.write(f'[HIGHEST_OVERHEAD] {overheads_max[0].upper()}: SGD{overheads_max[1]}\n')

        if coh_loss == []: #this means no loss occurred
            f.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for r in range(len(coh_loss)):
                f.write(f'[CASH DEFICIT] DAY: {coh_loss[r][0]}, AMOUNT: {coh_loss[r][0]}\n')

        if pnl_loss == []: #this means there were no losses
            f.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for r in range(len(pnl_loss)):
                f.write(f'[PROFIT DEFICIT] DAY: {pnl_loss[r][0]}, AMOUNT: {pnl_loss[r][1]}\n')
    
    print("output is successful")

main()
        
