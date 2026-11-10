@echo off
REM All git repos under c:\github, one "call :sync <folder> <url>" per line.
REM Clone repo_tools into the folder that should hold the repos and run this: missing repos
REM are cloned, existing ones are pulled (fast-forward only).
setlocal
cd /d "%~dp0.."
set FAILED=0

call :sync Claude-of-Duty https://github.com/mshumer/Claude-of-Duty
call :sync adaptive_academy https://github.com/rfernand2/adaptive_academy.git
call :sync book_factory2 https://github.com/rfernand2/book_factory2.git
call :sync book_tools https://github.com/rfernand2/book_tools.git
call :sync builder_gui https://github.com/rfernand2/builder_gui
call :sync claude_stocks https://github.com/rfernand2/claude_stocks.git
call :sync claude_tasks https://github.com/rfernand2/claude_tasks
call :sync control_center https://github.com/rfernand2/control_center
call :sync dc_lucas https://github.com/rfernand2/dc_lucas
call :sync dreamzone3 https://github.com/rfernand2/dreamzone3
call :sync dungeon_shooter https://github.com/rfernand2/dungeon_shooter.git
call :sync fps_trainer https://github.com/rfernand2/fps_trainer.git
call :sync galleries https://github.com/rfernand2/galleries.git
call :sync history_of_rock https://github.com/rfernand2/history_of_rock.git
call :sync hogans_alley https://github.com/rfernand2/hogans_alley.git
call :sync home_projects https://github.com/rfernand2/home_projects.git
call :sync house_ranker https://github.com/rfernand2/house_ranker.git
call :sync how_to https://github.com/rfernand2/how_to.git
call :sync lang_learn https://github.com/rfernand2/lang_learn.git
call :sync learn_to_draw https://github.com/rfernand2/learn_to_draw.git
call :sync lite_services https://github.com/rfernand2/lite_services.git
call :sync media_tracker https://github.com/rfernand2/media_tracker.git
call :sync monaco https://github.com/rfernand2/monaco.git
call :sync money_tracker https://github.com/rfernand2/money_tracker.git
call :sync mouse_track https://github.com/rfernand2/mouse_track
call :sync narrator https://github.com/rfernand2/narrator.git
call :sync old_book_factory https://github.com/rfernand2/book_factory.git
call :sync pencil https://github.com/rfernand2/pencil.git
call :sync portfolio_trader https://github.com/rfernand2/portfolio_trader.git
call :sync portfolios https://github.com/rfernand2/portfolios.git
call :sync powerpoint https://github.com/rfernand2/powerpoint
call :sync property_lines https://github.com/rfernand2/property_lines.git
call :sync quill https://github.com/rfernand2/quill
call :sync repo_tools https://github.com/rfernand2/repo_tools
call :sync retire_slider https://github.com/rfernand2/retire_slider.git
call :sync retirement https://github.com/rfernand2/retirement
call :sync sessions4 https://github.com/rfernand2/sessions4
call :sync solitaire https://github.com/rfernand2/solitaire
call :sync step_right https://github.com/rfernand2/step_right.git
call :sync studio https://github.com/rfernand2/studio
call :sync support_agent https://github.com/rfernand2/support_agent.git
call :sync vibe_wrangler https://github.com/rfernand2/vibe_wrangler.git
call :sync yellowsunsystems https://github.com/rfernand2/yellowsunsystems
call :sync books\berkeley_majors https://github.com/rf-books/berkeley_majors.git
call :sync books\delina_delaney https://github.com/rf-books/delina_delaney.git
call :sync books\delina_delaney_modern https://github.com/rf-books/delina_delaney_modern.git
call :sync books\franklin_book https://github.com/rf-books/franklin_book
call :sync books\franklin_shorts https://github.com/rf-books/franklin_shorts.git
call :sync books\girl_from_pismo https://github.com/rf-books/girl_from_pismo.git
call :sync books\gone_with_the_wind https://github.com/rf-books/gone_with_the_wind.git
call :sync books\lighthouse_keeper https://github.com/rf-books/lighthouse_keeper.git
call :sync books\love_in_excess https://github.com/rf-books/love_in_excess.git
call :sync books\marine_layer https://github.com/rf-books/marine_layer.git
call :sync books\my_brilliant_career https://github.com/rf-books/my_brilliant_career.git
call :sync books\old_cal_poly_majors https://github.com/rf-books/cal_poly_majors.git
call :sync books\rom_com_books https://github.com/rf-books/rom_com_books.git
call :sync books\the_castle_of_wolfenbach https://github.com/rf-books/the_castle_of_wolfenbach.git

echo.
if %FAILED%==0 (echo All repos up to date.) else (echo %FAILED% repo^(s^) need attention - see the output above.)
exit /b %FAILED%

:sync
echo === %~1
if exist "%~1\.git" (
  git -C "%~1" pull --ff-only
) else if exist "%~1" (
  echo Folder exists but is not a git repo - skipped.
  set /a FAILED+=1
  exit /b
) else (
  git clone "%~2" "%~1"
)
if errorlevel 1 set /a FAILED+=1
exit /b

REM Git repos with no remote (cannot be cloned, copy by hand):
REM   history_of_rock2
REM   books\modern_castle2
REM Folders that are not git repos (not synced, copy by hand):
REM   book_studio
REM   classics
REM   dc_lucas2
REM   dc_lucas3
REM   evolution_of_rock
REM   history_of_rock3
REM   history_of_sugar
REM   house_dreamer
REM   image_test
REM   on_the_beach
REM   orig_solitaire
REM   output
REM   test_books
REM   books\cal_poly_majors
REM   books\personalized
REM   books\public_domain
REM   books\wrong_side_of_road
REM   books\wrong_side_of_road2
